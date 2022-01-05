import typer
from pathlib import Path

import spacy


def update_config(treebank:str, wandb: bool):
    config_path = Path('config.cfg') 
    config_text = config_path.read_text()
    config_text = config_text.replace('\ntrain = null\n','\ntrain = "corpus/converted/train.spacy"\n')
    config_text = config_text.replace('\ndev = null\n','\ndev = "corpus/converted/dev.spacy"\n')
    if wandb:
        config_text = config_text.replace('\n\n[training.logger]\n@loggers = "spacy.ConsoleLogger.v1"\nprogress_bar = false\n\n',f'\n\n[training.logger]\n@loggers = "spacy.WandbLogger.v2"\nproject_name = "{treebank}"\nremove_config_values = []\nlog_dataset_dir = "./assets"\nmodel_log_interval = 1000\n\n')
    config_path.write_text(config_text)

if __name__ == "__main__":
    typer.run(update_config)
