from torchvision import transforms

from simple_resnet18 import SimpleResNet18
from simple_cnn import SimpleConvolutionalNetwork
from simple_mlp import SimpleMultiLayerPerceptron


class ModelFactory:
    """
    Factory class for creating predefined models adapted to FashionMNIST,
    along with their required data transforms and input adapters.

    Supported model types:
    - "simple_mlp"      : a multilayer perceptron (flattened 28x28 input)
    - "simple_cnn"      : a simple convolutional neural network
    - "simple_resnet18" : a ResNet18 backbone adapted to FashionMNIST
                          (with input resized and normalized as for ImageNet)

    Each factory call returns a 3-tuple:
    (model, transform, input_adapter)
    """

    @staticmethod
    def create_model_for_fashion_mnist(model_type = "simple_mlp"):
        """
        Create a model, preprocessing transform, and input adapter for FashionMNIST.

        Parameters
        ----------
        model_type : str, default="simple_mlp"
            Which architecture to build. One of:
            - "simple_mlp" to build SimpleMultiLayerPerceptron
            - "simple_cnn" to build SimpleConvolutionalNetwork
            - "simple_resnet18" to build SimpleResNet18

        Returns
        -------
        model : torch.nn.Module
            Instantiated model ready for training.
        transform : torchvision.transforms.Compose or callable
            Transform applied to FashionMNIST images when loading dataset.
        input_adapter : callable
            A function that adapts batch tensors into the correct input shape
            expected by the model (e.g., flatten for MLP).

        Raises
        ------
        ValueError
            If `model_type` is not recognized.
        """
        if model_type == "simple_mlp":
            model = SimpleMultiLayerPerceptron(input_size=28 * 28,
                                               hidden_layers=[256, 128],
                                               activation_type='relu',
                                               num_classes=10)
            # TODO - BLOCK START
            # TASK#7
            transform = None
            input_adapter = None
            # TODO - BLOCK END
            return model, transform, input_adapter

        elif model_type == "simple_cnn":
            model = SimpleConvolutionalNetwork(in_channels=1,
                                               activation_type='relu',
                                               num_classes=10)
            # TODO - BLOCK START
            # TASK#8
            transform = None
            input_adapter = None
            # TODO - BLOCK END
            return model, transform, input_adapter

        elif model_type == "simple_resnet18":
            model = SimpleResNet18(num_classes=10)
            # TODO - BLOCK START
            # TASK#9
            transform = None
            input_adapter = None
            # TODO - BLOCK END
            return model, transform, input_adapter

        raise ValueError(f"Unknown model name: {model_type}")

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