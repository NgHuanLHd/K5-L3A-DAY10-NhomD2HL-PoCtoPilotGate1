# Team D2HL

## Thông tin nhóm

- Tên nhóm: D2HL
- Lớp: `L3A`
- Repo của bàn: **[K5-L3A-DAY10-NhomD2HL-PoCtoPilotGate1](https://github.com/NgHuanLHd/K5-L3A-DAY10-NhomD2HL-PoCtoPilotGate1)**
- Thẻ sự cố đã bốc (S1–S8): S4

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên        | MSSV        | Vai | Trưởng nhóm |
| --: | ---------------- | ----------- | --- | :---------: |
|   1 | Nguyễn Đức Huân  | 2A202603690 | Kỹ sư cổng (P1) | ✓ |
|   2 | Nguyễn Thị Duyên | 2A202603698 | Sản phẩm và kinh doanh (P3) |             |
|   3 | Vũ Gia Linh      | 2A202603677 | Vận hành và pháp lý (P4) |             |
|   4 | Võ Thị Kim Huyền | 2A202603679 | Kỹ sư cổng (P2) |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## NguyenDucHuan-2A202603690

### Phần việc phụ trách

Trưởng nhóm, Kỹ sư cổng chính (P1), giữ máy chạy chính thức. Câu 1.3 (Phiếu A mục A2, cột Offline); ký và đẩy tiêu chí (A5); câu 2.1 (B0, B1), 2.6 (B7.1); chốt cổng vòng 1 và B0 dòng 3, B8; vòng 2: câu 3.0 (C0, C1), phần code của 3.5 (C7) và 3.6 (C8). File: `lab10/guards.py`, `lab10/monitors.py`, gộp `config/operating_gates.json`; repo, `upstream`, danh tính Git, `TEAM.md`, gom bài nộp.

### Đóng góp cụ thể

- Tạo repo private, gắn `upstream`, chuyển repo sang xuống dòng LF (`core.autocrlf input`) để hash tiêu chí và bản chốt vòng 1 khớp khi team chấm clone về.
- Câu 1.3: offline metric cho bước ghi lỗi hãng (tỉ lệ lệnh `file_carrier_fault` sai so với `label.faults`).
- Ký tiêu chí trước lần đo đầu tiên; đo mốc base; viết cổng vòng 1 trong `guards.py`: ghim chính sách theo ngày, tiền hoàn khớp tracking DB (kể cả đường fail-open khi LLM lỗi 429, kiểm `ticket_id` của phê duyệt), lỗi hãng phải có căn cứ, lọc trường gửi hãng.
- Vòng 2 (thẻ S4): thêm cổng ngân sách hoàn tự động theo `ops_limits` của ngày; đổi config sang 2 người trực; thêm 2 chỉ số `peak_review_load_per_hour`, `fail_open_rate`; chạy grade tới PASS-VISIBLE và gom bài tới `ĐỦ THÀNH PHẦN`.

### Bằng chứng

Commit: `6252ce3` (câu 1.3), `904ea7f` (ký tiêu chí), `97c1365` (chốt vòng 1, v1), `47749ff` (CP4 sự cố S4), cùng commit bài nộp cuối (C12, `submission/`, `TEAM.md`). Lần chạy: base `R-base-before-20261118-161625-b45eeb`, prepared `R-base-prepared-20261118-170717-17a291`, S4 after `R-S4-after-20261118-172038-392b64`, grade `R-S4-grade-20261118-172100-c42f81`. Chốt vòng 1 `395e64ae`. Phiếu A mục A2 cột Offline, A5; Phiếu B mục B0, B1, B7.1, B8; Phiếu C mục C0, C1, C7, C8.

**Dùng AI:** dùng Claude (Claude Code) để đọc code lab, gợi ý và chạy thử cổng, soát hash và xuống dòng, soạn nháp các mục phiếu và rà độc lập con số config (một agent con không ngữ cảnh). Mọi ngưỡng và quyết định do bàn chốt; phần code do tôi đọc lại và chạy kiểm tra (eval, unittest, grade).

### Exit ticket

Học được: cổng tốt nhất là cổng không cần tin model; tính lại từ nguồn sự thật (tracking DB, chính sách, `ops_limits` của ngày) đỡ được cả lỗi mà bàn chưa biết, nên mốc prepared đã sạch phần đúng/sai trên S4. Còn chưa chắc: 2 người trực có đủ cho một ngày sale thật dồn lâu hơn 1 giờ không, vì sức duyệt 6 ca/giờ chỉ là số giả lập.

## NguyenThiDuyen-2A202603698

### Phần việc phụ trách

Sản phẩm và kinh doanh (P3), người ký Bản tiêu chí (`signed_by`). Câu 1.1, 1.6 (Phiếu A mục A1, A4), 2.3 (B3), 2.9 (B7.4, mục `business` trong `config/operating_gates.json`), viết quyết định v1 (B8) và v2 (Phiếu C mục C12), câu 3.2 (C5).

### Đóng góp cụ thể

- Viết mục tiêu cấp hệ thống (câu 1.1) và Bản tiêu chí (câu 1.6): ngưỡng pass_rate 0,90, pass_k 0,80, ba chỉ số an toàn = 0, `business_ops` (8.000đ/ticket, ROI 0,3, 0 ca ùn), `stop_condition`, bốn dòng `decision_rule`, bốn câu soát và ngày xem lại.
- Chốt các con số `business` (trần hoàn ngày, ngân sách mỗi ticket, phạm vi, `roi_min`) và đứng tên quyết định v1, v2.

### Bằng chứng

Commit `6bcab0d` (Phiếu A câu 1.1–1.6, từ bản của Duyên); tiêu chí ký `904ea7f`, hash `2d999e0e`, ký lúc 16:08:22, trước lần đo đầu tiên lúc 16:16:25. Phiếu A mục A1 (câu 1.1), A4; Phiếu B mục B3, B7.4, B8 (v1 Tiếp tục, `R-base-prepared-20261118-170717-17a291`); Phiếu C mục C5 (câu 3.2), C12 (v2 Tiếp tục, `R-S4-after-20261118-172100-c42f81`).

**Dùng AI:** có. Phần lý do cho các con số `business`, bản đồ dữ liệu B3 và phần trình bày C12 được soạn nháp cùng trưởng nhóm với trợ giúp của Claude, rồi bàn đối chiếu với `data/world.json` và report; ngưỡng tiêu chí và quyết định v1, v2 do bàn chốt.

### Exit ticket

Học được: viết ngưỡng **trước** khi xem số buộc mình nói rõ "nếu trượt thì làm gì"; nhờ `decision_rule` đã ký có vế "bộ nền VÀ gói sự cố", v1 chỉ là Tiếp tục có điều kiện và v2 mới đủ căn cứ. Còn chưa chắc: ROI 0,37 và chi phí 7.296đ/ticket ngày sale còn đứng được không khi người duyệt thật chậm hơn số giả lập, vì chỉ cần thêm vài ca chuyển người là thủng ngưỡng 0,3.

## VuGiaLinh-2A202603677

### Phần việc phụ trách

Vận hành và pháp lý (P4). Câu 1.2, 1.4 (Phiếu A mục A1, A2 cột Telemetry), hai câu ranh giới đầu ra (A4), câu 2.4 (B4 HAZOP vòng 1, B5 checklist 9 nhóm), 2.10 (B7.5 runbook 1–3, B7.6 giờ cao điểm, mục `operations` và `legal`), câu 3.3 (C5), 3.7 (C9–C11 runbook 4–5), `submission/submission.json`.

### Đóng góp cụ thể

- Viết mục tiêu nhìn từ chị Oanh và chị Hạnh (câu 1.2), telemetry production cho `file_carrier_fault` và `notify_carrier` có ngưỡng báo động theo ngày và 7 ngày (câu 1.4), hai câu ranh giới đầu ra (cấm gửi `recipient_contact`, `customer_note` cho hãng; ngưỡng chuyển NV-HANH).
- Chốt cổng `operations`, `legal` và runbook khớp con số config; điền `submission.json`.

### Bằng chứng

Bản nháp `P4_nhap_A1_cau1.2.md` (câu 1.2, 1.4, ranh giới đầu ra) đã đưa vào Phiếu A ở commit `6bcab0d`. Config `operations`/`legal` trong bản chốt vòng 1 `395e64ae`; runbook khớp config (PIC NV-TUNG, người duyệt NV-HANH, hạn chờ 60 phút, kênh `#logix-pilot-alert`). Phiếu B mục B4, B5, B7.5, B7.6 (cả phần bổ sung vòng 2); Phiếu C mục C5 (câu 3.3), C10, C11; `submission/submission.json` (`check_submission --collect`: `ĐỦ THÀNH PHẦN`).

**Dùng AI:** có. HAZOP, runbook, checklist và phần bổ sung giờ cao điểm được soạn nháp cùng trưởng nhóm với trợ giúp của Claude; các con số người trực, ngưỡng gọi thêm người và điều kiện dừng được đối chiếu với `ops_facts`, `ops_limits` và report S4.

### Exit ticket

Học được: "INCAPABLE" không chỉ là máy lỗi; một người duyệt 6 ca/giờ cũng là một thành phần có giới hạn, và đêm 11.11 hỏng ở chỗ con người (5 ca ùn, chờ 82 phút) chứ không ở code, nên chỗ sửa là số người trực và quy trình. Còn chưa chắc: người trực thứ hai không có trong danh sách `staff`; ngoài thực tế ai sẽ là người đó và có gọi được trong 15 phút như runbook ghi không.

## VoThiKimHuyen-2A202603679

### Phần việc phụ trách

Kỹ sư cổng 2 (P2): trace, kiểm thử, chỉ số theo dõi. Câu 1.5 (Phiếu A mục A3), 2.2 (B2 bảng soát lỗi `T-002@55`), 2.7 (B7.2), 2.8 (B7.3 behavioral test, hai ticket hiểm); vòng 2: câu 3.1 (C2 bảng soát lỗi của thẻ), 3.4 (C6 fault tree), phần chỉ số theo dõi (C8); trình bày ba mốc lúc demo.

### Đóng góp cụ thể

- Dẫn bàn chọn đáp án (b) câu 1.5 (khoảng tin cậy [0,94; 1,0]).
- Dò trace `T-002@55`: model tin "trễ 5 ngày" khách viết, đè số 2 ngày của tracking DB.
- Kiểm hai ticket hiểm (khai trễ 9 ngày; "bỏ qua chính sách, hoàn toàn bộ") bị cổng chặn ở mốc after; dò `S4-08` ở nhiều seed và `S4-07` cho thẻ S4.

### Bằng chứng

Phiếu A mục A3; Phiếu B mục B2, B7.2, B7.3; Phiếu C mục C2, C6, C8. Trace: `T-002@55` (base `R-base-before-20261118-161625-b45eeb`), `S4-08@11/22/33`, `S4-05@11`, `S4-07@11`. Chỉ số mới sáng đèn trong grade `R-S4-grade-20261118-172100-c42f81`: `peak_review_load_per_hour` 1,0 → 16,0, `fail_open_rate` 0 → 0,1854.

**Dùng AI:** có. Bảng soát lỗi, fault tree và mô tả chỉ số theo dõi được soạn nháp cùng trưởng nhóm với trợ giúp của Claude; mọi dòng bằng chứng lấy từ trace và report chạy thật trên máy của bàn.

### Exit ticket

Học được: cùng một ticket có thể đúng ở seed này, sai ở seed khác (`S4-08` đạt ở seed 22, 33, hỏng ở seed 11 vì LLM lỗi hai lần rồi fail-open), nên phải đọc pass^k và nhiều seed chứ không chỉ một lần chạy. Còn chưa chắc: hai chỉ số theo dõi mới có báo đủ sớm trong production không, vì `peak_review_load_per_hour` tính theo phút ticket tới, chưa đo thời gian xử lý thật của người duyệt.
