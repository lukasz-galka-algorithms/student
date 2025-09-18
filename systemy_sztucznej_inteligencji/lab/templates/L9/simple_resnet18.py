import torch.nn as nn
from torchvision.models import resnet18, ResNet18_Weights

class SimpleResNet18(nn.Module):
    """
    A ResNet18 backbone adapted for FashionMNIST classification.

    Key steps to implement:
      - Load a pretrained ResNet18 (ImageNet weights).
      - Replace the final fully connected layer (fc) with a new Linear layer
        matching the number of classes (e.g., 10 for FashionMNIST).
      - Freeze all pretrained layers except the new fc layer
        (so only the classifier is trained).
    """

    def __init__(self, num_classes):
        """
        Initialize the ResNet18 model.

        Parameters
        ----------
        num_classes : int
            Number of output classes (FashionMNIST has 10).
        """
        super().__init__()
        # TODO - BLOCK START
        # TASK#6
        pass
        # TODO - BLOCK END

    def forward(self, x):
        """
        Forward pass.

        Parameters
        ----------
        x : torch.Tensor
            Input tensor of shape [B, 3, H, W], resized and normalized
            to match ImageNet preprocessing (e.g., [B, 3, 112, 112]).

        Returns
        -------
        torch.Tensor
            Logits of shape [B, num_classes].
        """
        return self.backbone(x)

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