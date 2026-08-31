from enum import StrEnum

class Mode(StrEnum):
    VULNERABLE = "vulnerable"
    BASIC = "basic"
    HARDENED = "hardened"

FAKE_TOKEN = "LAB_ONLY_7421"  # Synthetic lab marker; never use a real secret.
