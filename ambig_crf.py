# TODO: Add [PUNCT, PUNCT] to bundled tags
# TODO: Check whether I need to redefine backward
# TODO: Add mask for padded sequences
# TODO: Stop iterating over tensors - use tensor operations


import torch
import torch.nn as nn


class AmbigCRF(nn.Module):
    def __init__(self, num_tags: int):
        """
        CRF which runs on ambiguous labelling.

        :param num_tags: Number of unique bundled tags
        """
        super().__init__()
        self.transitions = nn.Parameter(torch.empty(num_tags, num_tags))
        self.start_transitions = nn.Parameter(torch.empty(num_tags))
        self.end_transitions = nn.Parameter(torch.empty(num_tags))

        self.reset_parameters()

    def reset_parameters(self) -> None:
        """Initialize the transition parameters.
        The parameters will be initialized randomly from a uniform distribution
        between -0.1 and 0.1.
        """
        nn.init.uniform_(self.start_transitions, -0.1, 0.1)
        nn.init.uniform_(self.end_transitions, -0.1, 0.1)
        nn.init.uniform_(self.transitions, -0.1, 0.1)

    def forward(self, inputs: torch.Tensor, tags: torch.Tensor):
        # shape: (batch_size,)
        numerator = self._compute_score(inputs, tags)
        # shape: (batch_size,)
        denominator = self._compute_normalizer(inputs)
        # shape: (batch_size,)
        llh = numerator - denominator
        return llh.sum()

    def decode(self):

    def calculate_features(self, sequence: torch.Tensor, tags: torch.Tensor):
        """

        :param sequence: The whole sentence
        :param tags: torch.Tensor([t_{i-1}, t_i])
        :return:
        """



    def _compute_score(self, inputs: torch.Tensor, tags: torch.Tensor) -> torch.Tensor:
        """
        Computes score which looks at adjacent elements of the sentence and summates over all of such pairs.
        Consists of 3 components: bundled tags (joint features), tags for one convention &
        tags for another convention (separate features for these two).

        :param inputs: Size = (batch_size, seq_len)
        :param tags: Size = (batch_size, 2, seq_len)
        :return:
        """

        score = 0

        # 1. Compute score for bundled tags

        # 2. Compute score for separate tags

        # Iterate over batch
        for i in range(inputs.size()[0]):
            # Iterate over two conventions
            for convention_num in range(tags.size()[1]):
                seq_score = self.start_transitions[tags[i, convention_num, 0]]


    def _compute_normalizer(self, inputs):