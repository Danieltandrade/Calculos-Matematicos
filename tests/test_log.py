"""
Testes para a função de logging do módulo `log`.
Verifica se os logs são registrados corretamente para os níveis INFO, WARNING e ERROR.
"""

import logging
from log import log

def test_log_info(caplog):
    """
    Testa se a função log registra corretamente mensagens de nível INFO.
    """
    with caplog.at_level(logging.INFO):
        log("INFO", "test_user", "Testando log de info", 42)

    assert "INFO" in caplog.text
    assert "test_user - Testando log de info - Resultado: 42" in caplog.text

def test_log_warning(caplog):
    """
    Testa se a função log registra corretamente mensagens de nível WARNING.
    """
    with caplog.at_level(logging.WARNING):
        log("WARNING", "test_user", "Testando log de warning", 100)

    assert "WARNING" in caplog.text
    assert "test_user - Testando log de warning - Resultado: 100" in caplog.text

def test_log_error(caplog):
    """
    Testa se a função log registra corretamente mensagens de nível ERROR.
    """
    with caplog.at_level(logging.ERROR):
        log("ERROR", "test_user", "Testando log de erro", None)

    assert "ERROR" in caplog.text
    assert "test_user - Testando log de erro" in caplog.text
