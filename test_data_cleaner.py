from data_cleaner import clean_name, clean_email, remove_empty_names

def test_clean_name():
    assert clean_name("   Ore   George   ") == "Ore George"

def test_clean_email():
    assert clean_email("  OREGEORGE@GMAIL.COM  ") == "oregeorge@gmail.com"

def test_remove_empty_names():
        names = ["Ore George", "", "   ", "Ada"]
        assert remove_empty_names(names) == ["Ore George", "Ada"]

def test_clean_name_empty():
        assert clean_name("") == ""

def test_clean_email_empty():
    assert clean_email("") == ""

def test_remove_empty_names_empty_list():
    assert remove_empty_names([]) == []

