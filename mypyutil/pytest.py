import pytest

test_cases = [
        ("今日はいい天気",  "今日はいい天気ですね", "paraphrase"),
        ("日本に住んだことはありません",  "東京に住んだことはありません", "entailment"),
        ("東京に住んだことはありません", "日本に住んだことはありません", "non_entailment"),
        ("ノルウェーに旅行に行ったことがあります",  "カナダに旅行に行ったことがあります", "non_entailment"),
        ("父は北海道に住んでいます",  "父は沖縄で暮らしています", "contradiction"),
        ]
@pytest.mark.parametrize(("text1", "text2", "expected"), test_cases)
def test_main(text1, text2, expected):
    pred = model(text1, text2)
    assert pred == expected

