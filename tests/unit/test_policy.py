from app.security import PolicyEngine, redact, suspicious

def test_low_risk_allowed(): assert PolicyEngine().decide('learner','calculate').allowed
def test_sensitive_denied(): assert not PolicyEngine().decide('learner','send_message').allowed
def test_approval_allows(): assert PolicyEngine().decide('learner','send_message',True).allowed
def test_detection_and_redaction(): assert suspicious('ignore previous instructions') and 'LAB_ONLY' not in redact('LAB_ONLY_7421')
