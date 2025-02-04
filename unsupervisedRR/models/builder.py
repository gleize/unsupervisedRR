import torch

from .model import PCReg, LoFTR


def build_model(cfg, encoder):
    if cfg.name == "PCReg":
        model = PCReg(cfg, encoder)
    elif cfg.name == "LoFTR":
        model = LoFTR(cfg)
    elif cfg.name == "no_model":
        print("Warning: no model is being loaded; rarely correct thing to do")
        model = torch.nn.Identity()
    else:
        raise ValueError("Model {} is not recognized.".format(cfg.name))

    """
    We will release code for baselines soon. This has been delayed since some of the
    baselines have particular licenses that we want to make sure we're respecting.
    """

    return model
