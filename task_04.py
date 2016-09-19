#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Too many cats fuctions"""


def too_many_kittens(kittens, litterboxes, catfood):
    """Test if there are too many kittens.

    Args:
        kittens (int): the number of kittens
        litterboxes (int): the number of litterboxes
        catfood (bool): where or not any catfood exists

    Returns:
        bool: if the number of kittens is greater than the number of litterboxes
              or there is no catfood available, return True. Else return false.

    Examples:
        >>>too_many_kittens(6,6, False)
        True

        >>>too_many_kittens(8,6, True)
        True

        >>>too_many_kittens(7,8, True)
        False
    """
    return not(litterboxes >= kittens and catfood)
