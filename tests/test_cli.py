from halloween.cli import main
import sys

def test_cli_runs(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["halloween", "ghost"])
    main()
    captured = capsys.readouterr()
    assert "o o" in captured.out