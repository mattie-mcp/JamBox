from app.nfc_daemon import format_tag_id


def test_format_tag_id():
    raw = bytes([0x04, 0xA2, 0x3B, 0x5C])
    assert format_tag_id(raw) == "04:A2:3B:5C"


def test_format_tag_id_single_byte():
    raw = bytes([0x0F])
    assert format_tag_id(raw) == "0F"
