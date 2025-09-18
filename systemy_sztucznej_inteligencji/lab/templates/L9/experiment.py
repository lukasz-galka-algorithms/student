import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets

from model_factory_for_fashionmnist import ModelFactory


class Experiment:
    """
    A step-based experiment runner for FashionMNIST using PyTorch models
    provided by `ModelFactory.create_model_for_fashion_mnist`.

    Supported steps (in `run_experiment`):
    - 'model'    : instantiate model + required transforms and input_adapter
    - 'data'     : build DataLoaders for train/test using the transform from the model factory
    - 'train'    : train the model for a given number of epochs
    - 'evaluate' : compute test-set accuracy
    """

    def __init__(self):
        """
        Initialize the experiment context.

        Attributes
        ----------
        device : torch.device
            Target device ('cuda' if available, otherwise 'cpu').
        pin_memory : bool
            Whether to enable pinned memory in DataLoaders (useful with CUDA).
        _num_classes : int
            Number of target classes for FashionMNIST (fixed to 10).
        _epochs_default : int
            Default number of epochs used in 'train' if not specified.
        _lr_default : float
            Default learning rate used in 'train' if not specified.

        Notes
        -----
        Members such as `model`, `transform`, `input_adapter`, `train_loader`,
        `test_loader`, `criterion` and `optimizer` are created lazily inside steps.
        """
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.pin_memory = True
        self._num_classes = 10
        self._epochs_default = 5
        self._lr_default = 1e-3

    def run_experiment(self, steps):
        """
        Run a series of experiment steps.

        Parameters
        ----------
        steps : list[tuple[str, dict]]
            Sequence of (step_name, params). Supported steps:
              - 'model':
                    params:
                        model_type : str, default 'simple_mlp'
                            One of: 'simple_mlp', 'simple_cnn', 'simple_resnet18'.
              - 'data':
                    params:
                        batch_size : int, default 128
                        num_workers : int, default 2
                        (pin_memory taken from self.pin_memory)
              - 'train':
                    params:
                        epochs : int, default self._epochs_default
                        learning_rate : float, default self._lr_default
              - 'evaluate':
                    no params required

        Returns
        -------
        list[tuple[str, any]]
            For each step returns a tuple of (step_name, result/info).
            Examples:
                ('model', 'Done')
                ('data', 'Done')
                ('train', {'epoch_losses': [ ... ]})
                ('evaluate', {'accuracy': 0.92})
        """
        results = []

        for step, params in steps:
            if step == 'model':
                model_type = params.get('model_type', 'simple_mlp')

                self.model, self.transform, self.input_adapter = ModelFactory.create_model_for_fashion_mnist(model_type)
                self.model = self.model.to(self.device)

                results.append((step, "Done"))

            elif step == 'data':
                batch_size = params.get('batch_size', 128)
                num_workers = params.get('num_workers', 2)
                pin_memory = self.pin_memory

                if self.transform is None or self.input_adapter is None or self.model is None:
                    results.append((step, "Error: No model found"))
                else:
                    train_ds = datasets.FashionMNIST('./data', train=True,  download=False, transform=self.transform)
                    test_ds  = datasets.FashionMNIST('./data', train=False, download=False, transform=self.transform)
                    # TODO - BLOCK START
                    # TASK#10

                    # TODO - BLOCK END
                    results.append((step, "Done"))

            elif step == 'train':
                if self.train_loader is None or self.test_loader is None:
                    results.append((step, "Error: No loader found"))
                elif self.model is None:
                    results.append((step, "Error: No model found"))
                else:
                    learning_rate = params.get('learning_rate', self._lr_default)
                    epochs = params.get('epochs', self._epochs_default)

                    self.criterion = nn.CrossEntropyLoss()
                    self.optimizer = torch.optim.Adam(self.model.parameters(), lr=learning_rate)

                    self.model.train()
                    epoch_losses = []

                    for epoch in range(1, epochs + 1):
                        running, seen = 0.0, 0
                        # TODO - BLOCK START
                        # TASK#11

                        # TODO - BLOCK END
                        avg_loss = running / max(1, seen)
                        epoch_losses.append(avg_loss)

                    results.append(
                        (step, {"epoch_losses": epoch_losses}))

            elif step == 'evaluate':
                if self.train_loader is None or self.test_loader is None:
                    results.append((step, "Error: No loader found"))
                elif self.model is None:
                    results.append((step, "Error: No model found"))
                else:
                    self.model.eval()
                    correct, total = 0, 0
                    with torch.no_grad():
                        # TODO - BLOCK START
                        # TASK#12
                        pass
                        # TODO - BLOCK END
                    results.append((step, {"accuracy": correct / total}))

            else:
                raise ValueError(f"Unknown step: {step}")

        return results

    @staticmethod
    def example_experiment_mlp():
        """
        FashionMNIST – MLP workflow:
        - Create model SimpleMultiLayerPerceptron (from ModelFactory)
        - Prepare data (batch_size=256, num_workers=2)
        - Train model (epochs=3, learning_rate=1e-3)
        - Evaluate model

        Returns
        -------
        list[tuple[str, any]]
            Step results for the entire workflow.
        """
        # TODO - BLOCK START
        # TASK#13
        steps = []
        # TODO - BLOCK END
        exp = Experiment()
        return exp.run_experiment(steps)

    @staticmethod
    def example_experiment_cnn():
        """
        FashionMNIST – CNN workflow:
        - Create model SimpleConvolutionalNetwork (from ModelFactory)
        - Prepare data (batch_size=256, num_workers=2)
        - Train model (epochs=3, learning_rate=1e-3)
        - Evaluate model

        Returns
        -------
        list[tuple[str, any]]
            Step results for the entire workflow.
        """
        # TODO - BLOCK START
        # TASK#14
        steps = []
        # TODO - BLOCK END
        exp = Experiment()
        return exp.run_experiment(steps)

    @staticmethod
    def example_experiment_resnet18():
        """
        FashionMNIST – ResNet18 workflow:
        - Create model SimpleResNet18
        - Prepare data (batch_size=256, num_workers=2)
        - Train model (epochs=1, learning_rate=1e-4)
        - Evaluate model

        Returns
        -------
        list[tuple[str, any]]
            Step results for the entire workflow.
        """
        # TODO - BLOCK START
        # TASK#15
        steps = []
        # TODO - BLOCK END
        exp = Experiment()
        return exp.run_experiment(steps)

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