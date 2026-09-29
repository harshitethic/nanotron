from types import SimpleNamespace

from nanotron.data.nemo_dataset.blendable_dataset import BlendableDataset


def test_get_consumption_stats_supports_local_and_s3_paths():
    dataset = BlendableDataset.__new__(BlendableDataset)
    dataset.datasets = [
        SimpleNamespace(folder_path="/data/local-dataset"),
        SimpleNamespace(folder_path="s3://bucket/remote-dataset"),
    ]
    dataset.consumed_tokens = {0: 128, 1: 256}

    assert dataset.get_consumption_stats() == {
        "/data/local-dataset": {"tokens": 128},
        "s3://bucket/remote-dataset": {"tokens": 256},
    }
