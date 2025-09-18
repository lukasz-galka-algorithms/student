import torch.nn as nn

def get_activation_function(activation_type):
    """
    Return an activation module by name.

    Parameters
    ----------
    activation_type : {'relu', 'sigmoid', 'tanh'}
        Name of the activation to use.

    Returns
    -------
    nn.Module
        Corresponding activation module.

    Raises
    ------
    ValueError
        If the activation name is not supported.
    """
    # TODO - BLOCK START
    # TASK#4
    pass
    # TODO - BLOCK END

class SimpleConvolutionalNetwork(nn.Module):
    """
    Simple CNN for FashionMNIST (input: [B, 1, 28, 28]).

    Target architecture (to be implemented):
      Block 1:
        Conv(1→32, kernel=3, padding=1) → Activation
        Conv(32→64, kernel=3, padding=1) → Activation
        MaxPool2d(2)                     # 28x28 → 14x14
        Dropout(p=0.25)

      Block 2:
        Conv(64→128, kernel=3, padding=1) → Activation
        MaxPool2d(2)                      # 14x14 → 7x7

      Classifier:
        Flatten()                         # [B, 128, 7, 7] → [B, 128*7*7]
        Linear(128*7*7 → 128) → Activation → Dropout(p=0.5)
        Linear(128 → num_classes)         # logits, no Softmax (CrossEntropyLoss expects logits)

    Wrap all layers into a single sequential module.
    """
    def __init__(self, in_channels=1, activation_type='relu', num_classes=10):
        """
        Initialize the CNN layers.

        Parameters
        ----------
        in_channels : int, default=1
            Number of input channels (1 for grayscale FashionMNIST).
        activation_type : {'relu','sigmoid','tanh'}, default='relu'
            Activation function used after each conv and the first linear layer.
        num_classes : int, default=10
            Number of output classes (FashionMNIST has 10).
        """
        super(SimpleConvolutionalNetwork, self).__init__()

        layers = []

        # TODO - BLOCK START
        # TASK#5

        # TODO - BLOCK END
        self.network = nn.Sequential(*layers)

    def forward(self, x):
        """
        Forward pass.

        Parameters
        ----------
        x : torch.Tensor
            Input tensor of shape [B, 1, 28, 28].

        Returns
        -------
        torch.Tensor
            Logits of shape [B, num_classes].
        """
        return self.network(x)

class StudentID:
    """
    Utility class for identifying the student.

    Each student must replace the placeholder return value
    in the `get_ID` method with their own unique student ID.
    """

    @staticmethod
    def get_ID():
        """
        Return the student ID as a string.

        Returns
        -------
        str
            The student ID. Each student must replace "student_ID" with their own ID.

        Examples
        --------
        >>> StudentID.get_ID()
        '123456'
        """
        # TODO - BLOCK START
        # TASK#1
        return "student_ID"
        # TODO - BLOCK END