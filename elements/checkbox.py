"""This module contains an implementation of a checkbox type of element in a given UI."""
from __future__ import annotations

import logging
from typing import Optional, Tuple, Union

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from elements.base_web_element import BaseWebElement
from settings import LOGGING_LEVEL

logging.basicConfig(level=LOGGING_LEVEL)


class Checkbox(BaseWebElement):
    """This class implements an abstraction of a checkbox type of element in a UI."""

    # A default CSS selector to allow for a simpler interface where the user only passes the
    # parent element. Set the value to a common selector for checkbox elements in your project
    DEFAULT_CSS_SELECTOR = 'label> input[type="checkbox"]'

    def __init__(
        self,
        parent: Optional[Union[BaseWebElement, WebElement, WebDriver]] = None,
        locator: Optional[Tuple[By, str]] = None,
        web_element: Optional[WebElement] = None,
    ):
        # pylint: disable=duplicate-code
        if not (locator or web_element):
            super().__init__(
                parent=parent,
                locator=(By.CSS_SELECTOR, type(self).DEFAULT_CSS_SELECTOR),
            )
        else:
            super().__init__(parent=parent, locator=locator, web_element=web_element)

    def is_checked(self) -> bool:
        """Determines whether the checkbox is checked or not

        Returns
        -------
        bool
        """
        return self.find_element().is_selected()

    def check(self) -> Checkbox:
        """Checks the checkbox if it's not already checked.

        Returns
        -------
        Checkbox
            Returns the instance itself to allow for a fluent interface.
        """
        if not self.is_checked():
            self.click()
            logging.info("Checked checkbox element with locator: %s", self.locator)
        return self

    def uncheck(self) -> Checkbox:
        """Unchecks the checkbox if it's already checked.

        Returns
        -------
        Checkbox
            Returns the instance itself to allow for a fluent interface.
        """
        if self.is_checked():
            self.click()
            logging.info("Unchecked checkbox element with locator: %s", self.locator)
        return self
