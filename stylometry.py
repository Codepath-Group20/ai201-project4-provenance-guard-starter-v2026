"""
Signal two: the style signal. — Updated implementation
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


def sentence_length_spread(text: str) -> float:
    s_list = sentences(text)
    if len(s_list) <= 1:
        return 0.2  # Default baseline for single/short text
    
    lengths = [len(words(s)) for s in s_list]
    mean_len = statistics.mean(lengths)
    if mean_len == 0:
        return 0.0
        
    try:
        stdev_len = statistics.stdev(lengths)
        return stdev_len / mean_len
    except statistics.StatisticsError:
        return 0.0


def type_token_ratio(text: str) -> float:
    w_list = words(text)
    if not w_list:
        return 0.0
    return len(set(w_list)) / len(w_list)


def punctuation_density(text: str) -> float:
    if not text.strip():
        return 0.0
    punct_chars = re.findall(r"[,;:\-?!]", text)
    return len(punct_chars) / len(text)


def style_signal(text: str) -> float:
    s_spread = sentence_length_spread(text)
    ttr = type_token_ratio(text)
    p_density = punctuation_density(text)

    # Normalized component scoring (higher = more AI-like)
    spread_ai_score = max(0.0, min(1.0, 1.0 - s_spread))
    ttr_ai_score = max(0.0, min(1.0, 1.0 - ttr))
    p_score = max(0.0, min(1.0, p_density * 15.0))

    combined = (spread_ai_score * 0.4) + (ttr_ai_score * 0.4) + (p_score * 0.2)
    return round(max(0.1, min(0.9, combined)), 4)


if __name__ == "__main__":
    import sys
    text = " ".join(sys.argv[1:]) or "Test sentence one. Test sentence two here."
    print(f"style_signal: {style_signal(text)}")
