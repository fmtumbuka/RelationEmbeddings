# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#        Copyright (c) -2023 - Mtumbuka F.                                                       #
#        All rights reserved.                                                                       #
#                                                                                                   #
#        Redistribution and use in source and binary forms, with or without modification, are       #
#        permitted provided that the following conditions are met:                                  #    
#        1. Redistributions of source code must retain the above copyright notice, this list of     #
#           conditions and the following disclaimer.                                                #
#        2. Redistributions in binary form must reproduce the above copyright notice, this list of  #
#           conditions and the following disclaimer in the documentation and/or other materials     #
#           provided with the distribution.                                                         #
#                                                                                                   #
#        THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS \"AS IS\" AND ANY      #
#        EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF    #
#        MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE #
#        COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,   #
#        EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF         #
#        SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)     #
#        HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR   #
#        TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS         #
#        SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.                               #
#                                                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


__license__ = "BSD-2-Clause"
__version__ = "2023.1"
__date__ = "06 Mar 2023"
__author__ = "Frank M. Mtumbuka"
__maintainer__ = "Frank M. Mtumbuka"
__email__ = "" ""
__status__ = "Development"

import abc
import typing
import datapipeline.pretraining_pairs as pretraining_pairs
import datapipeline.relation_input_example as relation_input_example
import os
import spacy


class BaseDataLoader(metaclass=abc.ABCMeta):
    """This is the base class all data loaders will extend."""

    def __init__(self, data_path: str, pretrain: bool = False):
        """
        This creates an instance of the `BaseDataLoader`.
        Args:
            data_path (str): The path to the data directory
            pretrain (bool): Specifies whether to load pretraining data or not.
        """

        # Check if the provided path refers to a file on the system.
        if not os.path.isdir(data_path):
            raise ValueError("The supplied data path does not refer to a directory on the system.")

        self._data_path = data_path
        self._nlp = spacy.load("en_core_web_sm")

    @abc.abstractmethod
    def load(self) -> typing.Union[
        typing.List[relation_input_example.RelationInputExample],
        typing.List[pretraining_pairs.SentencePairs]
    ]:
        """
        This reads data from a specified file and loads it into memory.
        Returns:
            stories (::class:`story.Story`)
        """
