from functools import wraps
from main import session, request, url_for


def login_required(f): # 원하는 함수 위에 설정하면 로그인 안했을 시 접근 막음
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if session.get("id") is None or session.get("id") == "":
      return redirect(url_for("member_login", next_url=request.url))
    return f(*args, **kwargs)
  return decorated_function