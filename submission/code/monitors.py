"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def peak_review_load_per_hour(trials):
    """Vận hành (S4): số ca vào hàng chờ người duyệt nhiều nhất trong một cửa sổ 60 phút bất kỳ của một ngày vận hành
    (trung bình qua các seed). So với sức duyệt: 1 người = 6 ca/giờ. Không cần nhãn."""
    days = {}
    for t in trials:
        if t.get("review_kind") and t.get("arrive_min") is not None:
            days.setdefault((t.get("seed"), t.get("day")), []).append(t["arrive_min"])
    if not days:
        return 0.0
    peaks = []
    for mins in days.values():
        mins.sort()
        peaks.append(max(sum(1 for m in mins if start <= m < start + 60) for start in mins))
    return round(sum(peaks) / len(peaks), 2)


def fail_open_rate(trials):
    """Kỹ thuật (S4): tỉ lệ trial mà LLM lỗi ở bước kiểm chính sách và agent rơi vào đường 'fail-open'
    (hoàn phí ship không qua kiểm). Không cần nhãn: đọc sự kiện llm_fallback trong trace."""
    hit = sum(any(e.get("type") == "llm_fallback" and e.get("mode") == "fail_open" for e in t["events"])
              for t in trials)
    return round(hit / max(1, len(trials)), 4)


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "peak_review_load_per_hour": peak_review_load_per_hour,
    "fail_open_rate": fail_open_rate,
}
STARTER_MONITORS = ("escalation_rate",)
