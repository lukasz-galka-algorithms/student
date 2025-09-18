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
    # TASK#2
    pass
    # TODO - BLOCK END

class SimpleMultiLayerPerceptron(nn.Module):
    """
    Simple fully connected neural network (MLP).

    Input shape: [B, input_size] where input_size = 28*28 for FashionMNIST.

    Target architecture (to be implemented by the student):
      - Linear(input_size → hidden1) → Activation
      - Linear(hidden1 → hidden2) → Activation
      - ...
      - Linear(last_hidden → num_classes)

    The number and size of hidden layers is configurable via the `hidden_layers` list.
    Wrap all layers into a single sequential module.
    """

    def __init__(self, input_size, hidden_layers, activation_type, num_classes):
        """
        Initialize the MLP layers.

        Parameters
        ----------
        input_size : int
            Number of input features (e.g. 784 for 28x28 FashionMNIST).
        hidden_layers : list[int]
            Sizes of hidden layers, e.g. [256, 128].
        activation_type : {'relu','sigmoid','tanh'}
            Activation function applied after each hidden Linear layer.
        num_classes : int
            Number of output classes (FashionMNIST has 10).
        """
        super(SimpleMultiLayerPerceptron, self).__init__()

        layers = []
        # TODO - BLOCK START
        # TASK#3

        # TODO - BLOCK END
        self.network = nn.Sequential(*layers)

    def forward(self, x):
        """
        Forward pass.

        Parameters
        ----------
        x : torch.Tensor
            Input tensor of shape [B, input_size].

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