import streamlit as st
import random

st.set_page_config(
    page_title="Ôn tập Pháp luật đại cương EM1170 - HUST",
    page_icon="⚖️",
    layout="wide"
)

# Cấu trúc dữ liệu: (Chủ đề, Nguồn, Câu hỏi, [Đáp án A, B, C, D hoặc Đúng, Sai], Index đáp án đúng (0-based), Giải thích)
QUESTIONS_DB = [
    # =========================================================================
    # PHẦN 1: CÂU HỎI ĐÚNG / SAI CÓ GIẢI THÍCH (CLB HTHT - GIỮA KỲ)
    # =========================================================================
    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 1 (Câu 1)",
     "Pháp luật đại cương là một ngành khoa học pháp lý trong hệ thống các khoa học pháp lý cơ bản.",
     ["Đúng", "Sai"], 0,
     "Pháp luật đại cương là một chuyên ngành khoa học pháp lý cung cấp những kiến thức cơ bản nhất (đại cương), có tính chất nền tảng cho việc nhận thức những tri thức đối với nhiều lĩnh vực khoa học trong hệ thống khoa học pháp lý."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 1 (Câu 2)",
     "Pháp luật đại cương nghiên cứu về các vấn đề cơ bản của nhà nước và pháp luật.",
     ["Đúng", "Sai"], 0,
     "Pháp luật đại cương cung cấp kiến thức tổng quan về nhà nước và pháp luật mang tính cơ bản cho các khoa học pháp lý chuyên ngành và khoa học pháp lý ứng dụng."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 1 (Câu 3)",
     "Lịch sử hình thành nhà nước và pháp luật là đối tượng nghiên cứu của pháp luật đại cương.",
     ["Đúng", "Sai"], 0,
     "Pháp luật đại cương nghiên cứu Nhà nước trên phương diện một hiện tượng xã hội – lịch sử gắn liền với Pháp luật, song hành cùng Pháp luật."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 1 (Câu 4)",
     "Đối tượng nghiên cứu của pháp luật đại cương là nghiên cứu đồng thời Nhà nước và Pháp luật trong mối quan hệ qua lại hữu cơ với nhau.",
     ["Đúng", "Sai"], 0,
     "Pháp luật đại cương nghiên cứu Nhà nước trên phương diện một hiện tượng xã hội – lịch sử gắn liền với Pháp luật, song hành cùng Pháp luật. Không thể nghiên cứu về Pháp luật nếu không xem xét đến Nhà nước."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 1 (Câu 5)",
     "Pháp luật đại cương không nghiên cứu các hệ thống pháp luật trên thế giới.",
     ["Đúng", "Sai"], 1,
     "Sai. Đối tượng nghiên cứu của pháp luật đại cương bao gồm hệ thống pháp luật thế giới và Việt Nam."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 1 (Câu 6)",
     "Pháp luật đại cương trả lời câu hỏi: Vai trò của nhà nước hình thành để làm gì?",
     ["Đúng", "Sai"], 0,
     "Pháp luật đại cương cung cấp những kiến thức tổng thể và khái quát nhất mang tính lý luận về Nhà nước và Pháp luật, trả lời câu hỏi nhà nước và pháp luật là gì, xuất hiện từ bao giờ, như thế nào và để làm gì."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 1 (Câu 7)",
     "Pháp luật đại cương là nền tảng, cung cấp những kiến thức cơ sở cho nhiều ngành khoa học pháp lý khác.",
     ["Đúng", "Sai"], 0,
     "Pháp luật đại cương cung cấp kiến thức cơ sở ngành cho khối ngành khoa học xã hội - nhân văn, kinh tế, luật."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 1 (Câu 8)",
     "Pháp luật đại cương cung cấp các kiến thức chuyên sâu về những vấn đề liên quan đến Nhà nước và Pháp luật.",
     ["Đúng", "Sai"], 1,
     "Sai. Pháp luật đại cương chỉ cung cấp những kiến thức tổng thể và khái quát nhất mang tính lý luận cơ bản về Nhà nước và Pháp luật, không phải kiến thức chuyên sâu."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 1 (Câu 9)",
     "Pháp luật đại cương cung cấp những kiến thức phổ thông nhằm giáo dục và phổ biến pháp luật cho mọi công dân.",
     ["Đúng", "Sai"], 0,
     "Môn học Pháp luật đại cương cung cấp những kiến thức pháp luật căn bản cho mỗi công dân để đáp ứng yêu cầu xây dựng Nhà nước pháp quyền và phát triển kinh tế - xã hội."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 2 (Câu 14)",
     "Kiểu nhà nước là cách thức tổ chức quyền lực nhà nước và những phương pháp để thực hiện quyền lực nhà nước.",
     ["Đúng", "Sai"], 1,
     "Sai. Cách thức tổ chức quyền lực nhà nước và phương pháp thực hiện quyền lực nhà nước thể hiện thông qua hình thức nhà nước (và chế độ chính trị), không phải kiểu nhà nước."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 2 (Câu 16)",
     "Chức năng lập pháp của nhà nước là hoạt động xây dựng pháp luật và tổ chức thực hiện pháp luật.",
     ["Đúng", "Sai"], 1,
     "Sai. Chức năng lập pháp của nhà nước là hoạt động xây dựng pháp luật và ban hành pháp luật. Tổ chức thực hiện pháp luật là chức năng hành pháp."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 2 (Câu 17)",
     "Chức năng hành pháp của nhà nước là hoạt động nhằm bảo đảm cho pháp luật được thực hiện nghiêm minh và bảo vệ pháp luật trước những hành vi vi phạm.",
     ["Đúng", "Sai"], 1,
     "Sai. Hoạt động bảo vệ pháp luật trước những hành vi vi phạm là chức năng của tư pháp."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 2 (Câu 18)",
     "Chức năng tư pháp của nhà nước là mặt hoạt động bảo vệ pháp luật.",
     ["Đúng", "Sai"], 0,
     "Đúng. Hoạt động bảo vệ pháp luật trước những hành vi vi phạm là chức năng của tư pháp."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 2 (Câu 25)",
     "Nhà nước là chủ thể duy nhất có quyền ban hành pháp luật và quản lý xã hội bằng pháp luật.",
     ["Đúng", "Sai"], 0,
     "Đúng. Pháp luật do nhà nước ban hành có tính bắt buộc chung. Các tổ chức khác chỉ được quyền ban hành điều lệ, quy chế có hiệu lực nội bộ."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 2 (Câu 27)",
     "Thông qua hình thức nhà nước biết được ai là chủ thể nắm quyền lực nhà nước và việc tổ chức thực thi quyền lực Nhà nước như thế nào.",
     ["Đúng", "Sai"], 0,
     "Đúng. Hình thức nhà nước là cách tổ chức bộ máy quyền lực nhà nước và phương pháp thực hiện quyền lực nhà nước."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 2 (Câu 28)",
     "Căn cứ hình thức chính thể Nhà nước, ta biết được Nhà nước đó có dân chủ hay không.",
     ["Đúng", "Sai"], 1,
     "Sai. Muốn biết nhà nước có dân chủ hay không phải thông qua chế độ chính trị để biết các phương pháp, cách thức thực hiện quyền lực nhà nước."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 2 (Câu 29)",
     "Trong hình thức chính thể quân chủ thì quyền lực tối cao của nhà nước thuộc một tổ chức được nhân dân bầu ra.",
     ["Đúng", "Sai"], 1,
     "Sai. Trong chính thể quân chủ, quyền lực cao nhất tập trung toàn bộ hay một phần vào tay người đứng đầu nhà nước theo nguyên tắc thừa kế (vua, quốc vương, hoàng đế)."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 2 (Câu 30)",
     "Chế độ chính trị là toàn bộ các phương pháp, cách thức thực hiện quyền lực nhà nước.",
     ["Đúng", "Sai"], 0,
     "Đúng. Chế độ chính trị là toàn bộ các phương pháp, thủ đoạn, cách thức mà giai cấp thống trị sử dụng để thực hiện quyền lực nhà nước của mình."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 3 (Câu 1)",
     "Nhà nước CHXHCN Việt Nam có hình thức cấu trúc nhà nước đơn nhất.",
     ["Đúng", "Sai"], 0,
     "Đúng. Nhà nước Việt Nam có chủ quyền duy nhất, có một hệ thống cơ quan nhà nước và một hệ thống pháp luật thống nhất."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 3 (Câu 2)",
     "Cơ quan nhà nước có nhiệm vụ, quyền hạn mang tính quyền lực nhà nước.",
     ["Đúng", "Sai"], 0,
     "Đúng. Cơ quan nhà nước là bộ phận cấu thành của bộ máy nhà nước, được thành lập và có thẩm quyền theo quy định của pháp luật nhằm thực hiện chức năng nhà nước."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 3 (Câu 3)",
     "Bộ máy nhà nước là tập hợp các cơ quan nhà nước từ trung ương đến địa phương.",
     ["Đúng", "Sai"], 0,
     "Đúng. Bộ máy nhà nước XHCN là hệ thống các cơ quan nhà nước từ trung ương xuống địa phương, tổ chức và hoạt động theo những nguyên tắc chung thống nhất."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 3 (Câu 4)",
     "Cơ quan nhà nước làm việc theo chế độ tập thể trước khi biểu quyết phải thảo luận dân chủ, quyết định theo đa số.",
     ["Đúng", "Sai"], 0,
     "Đúng. Cơ quan nhà nước làm việc theo chế độ tập thể trước khi biểu quyết phải thảo luận tập thể và biểu quyết theo đa số."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 3 (Câu 5)",
     "Quốc hội là cơ quan hành chính nhà nước cao nhất của nước CHXHCN Việt Nam.",
     ["Đúng", "Sai"], 1,
     "Sai. Chính phủ mới là cơ quan hành chính nhà nước cao nhất của nước CHXHCN Việt Nam."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 3 (Câu 6)",
     "Quốc hội là cơ quan đại biểu cao nhất của nhân dân.",
     ["Đúng", "Sai"], 0,
     "Đúng. Quốc hội là cơ quan đại biểu cao nhất của nhân dân, cơ quan quyền lực nhà nước cao nhất của nước CHXHCN Việt Nam."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 3 (Câu 7)",
     "Quốc hội là cơ quan quyền lực nhà nước cao nhất của nước CHXHCN Việt Nam.",
     ["Đúng", "Sai"], 0,
     "Đúng. Quốc hội là cơ quan duy nhất có quyền lập hiến, lập pháp, quyết định những chính sách cơ bản về đối nội, đối ngoại và giám sát tối cao đối với toàn bộ hoạt động của Nhà nước."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 3 (Câu 8)",
     "Chủ tịch nước không bắt buộc phải là đại biểu Quốc hội.",
     ["Đúng", "Sai"], 1,
     "Sai. Chủ tịch nước do Quốc hội bầu ra trong số các đại biểu Quốc hội."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 3 (Câu 9)",
     "Chủ tịch nước là người đứng đầu nhà nước, có quyền quyết định các vấn đề quan trọng của đất nước.",
     ["Đúng", "Sai"], 1,
     "Sai. Thẩm quyền quyết định các vấn đề quan trọng của đất nước thuộc về Quốc hội."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 3 (Câu 10)",
     "Chính phủ là cơ quan đại diện của nhân dân, do cử tri cả nước trực tiếp bầu ra.",
     ["Đúng", "Sai"], 1,
     "Sai. Quốc hội mới là cơ quan đại biểu cao nhất của nhân dân do cử tri bầu ra, còn Chính phủ là cơ quan chấp hành của Quốc hội."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 3 (Câu 11)",
     "Thủ tướng Chính phủ do Chủ tịch nước bổ nhiệm, miễn nhiệm, bãi nhiệm.",
     ["Đúng", "Sai"], 1,
     "Sai. Thủ tướng Chính phủ do Quốc hội bầu, miễn nhiệm, bãi nhiệm theo đề nghị của Chủ tịch nước. Thủ tướng phải là đại biểu Quốc hội."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 3 (Câu 12)",
     "Bộ trưởng, thủ trưởng cơ quan ngang bộ là người đứng đầu Chính phủ, do các thành viên Chính phủ trực tiếp bầu ra.",
     ["Đúng", "Sai"], 1,
     "Sai. Thủ tướng Chính phủ là người đứng đầu Chính phủ. Các Bộ trưởng, Thủ trưởng cơ quan ngang bộ do Thủ tướng đề nghị Quốc hội phê chuẩn việc bổ nhiệm, miễn nhiệm, cách chức."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 3 (Câu 13a)",
     "Hội đồng nhân dân là cơ quan hành chính nhà nước ở địa phương, do nhân dân địa phương bầu ra.",
     ["Đúng", "Sai"], 1,
     "Sai. Hội đồng nhân dân là cơ quan quyền lực nhà nước ở địa phương. Ủy ban nhân dân mới là cơ quan hành chính nhà nước ở địa phương."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 3 (Câu 13b)",
     "Ủy ban nhân dân địa phương có quyền ban hành nghị định và quyết định.",
     ["Đúng", "Sai"], 1,
     "Sai. Ủy ban nhân dân địa phương chỉ có quyền ban hành quyết định. Nghị định là văn bản do Chính phủ ban hành."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 3 (Câu 14)",
     "Tòa án nhân dân và Viện Kiểm sát nhân dân là hai cơ quan duy nhất có chức năng xét xử của nhà nước ta.",
     ["Đúng", "Sai"], 1,
     "Sai. Cơ quan duy nhất thực hiện chức năng xét xử là Tòa án nhân dân. Viện Kiểm sát nhân dân thực hiện quyền công tố và kiểm sát hoạt động tư pháp."),

    ("1. Câu hỏi Đúng/Sai (Có giải thích)", "Đúng/Sai - Chương 3 (Câu 15)",
     "Đảng Cộng sản Việt Nam là một cơ quan trong bộ máy nhà nước CHXHCN Việt Nam.",
     ["Đúng", "Sai"], 1,
     "Sai. Đảng Cộng sản Việt Nam là một bộ phận (lực lượng lãnh đạo) trong Hệ thống chính trị, không phải là một cơ quan trong Bộ máy nhà nước."),

    # =========================================================================
    # PHẦN 2: HỆ THỐNG CHÍNH TRỊ VÀ BỘ MÁY NHÀ NƯỚC VIỆT NAM
    # =========================================================================
    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC1 - Câu 9 & PLDC6 - Câu 28",
     "Tổ chức nào sau đây đóng vai trò là trung tâm của hệ thống chính trị Việt Nam?",
     ["A. Đảng phái chính trị (Đảng Cộng sản Việt Nam)", "B. Các tổ chức chính trị - xã hội", "C. Nhà nước", "D. Các tổ chức xã hội, xã hội nghề nghiệp"], 2,
     "Nhà nước đóng vai trò là trụ cột, trung tâm của hệ thống chính trị Việt Nam (Đảng Cộng sản Việt Nam là lực lượng lãnh đạo)."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC1 - Câu 12 & PLDC7 - Câu 22",
     "Nhà nước nào sau đây có hình thức cấu trúc nhà nước liên bang?",
     ["A. Việt Nam", "B. Pháp", "C. Ấn Độ", "D. Trung Quốc"], 2,
     "Việt Nam, Pháp, Trung Quốc có cấu trúc nhà nước đơn nhất; Ấn Độ là nhà nước liên bang."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC1 - Câu 14 & PLDC9 - Câu 15",
     "Học thuyết được một số quốc gia trên thế giới áp dụng trong việc tổ chức bộ máy nhà nước là học thuyết nào?",
     ["A. Thuyết tam quyền phân lập", "B. Thuyết Hàn Phi Tử", "C. Thuyết bạo lực", "D. Thuyết khế ước xã hội"], 0,
     "Thuyết phân quyền (tam quyền phân lập) chia quyền lực nhà nước thành lập pháp, hành pháp và tư pháp."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC1 - Câu 15 & PLDC4 - Câu 3",
     "Đâu là đặc trưng của nhà nước pháp quyền?",
     ["A. Sự thống trị của pháp luật trong mọi lĩnh vực của đời sống xã hội", "B. Sự ràng buộc của Nhà nước, cơ quan nhà nước, công chức nhà nước bởi pháp luật", "C. Xác định rõ trách nhiệm của nhà nước và công dân trên cơ sở pháp luật", "D. Tất cả các đáp án trên"], 3,
     "Cả 3 đặc trưng trên đều là dấu hiệu cốt lõi của nhà nước pháp quyền."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC1 - Câu 22 & PLDC8 - Câu 15, 29",
     "Hội đồng nhân dân các cấp có quyền ban hành loại văn bản quy phạm pháp luật nào?",
     ["A. Nghị quyết", "B. Nghị định", "C. Nghị quyết, nghị định", "D. Nghị quyết, quyết định"], 0,
     "Theo Luật Ban hành VBQPPL, Hội đồng nhân dân các cấp ban hành Nghị quyết (Ủy ban nhân dân ban hành Quyết định)."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC2 - Câu 23 & PLDC1 - Câu 7",
     "Nhà nước phong kiến Việt Nam ghi nhận những tư tưởng của tôn giáo nào?",
     ["A. Thiên chúa giáo", "B. Phật giáo", "C. Nho giáo", "D. Cả Phật giáo và Nho giáo (Tùy từng giai đoạn mà Nho giáo giữ vai trò thống trị)"], 3,
     "Trong PLDC2 đáp án là Cả Phật giáo và Nho giáo (câu 23); trong PLDC1 (câu 7) khi hỏi sự thống trị về tư tưởng thì đáp án là Nho giáo."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC3 - Câu 3",
     "Chế độ chính trị của nhà nước Việt Nam là gì?",
     ["A. Dân chủ quý tộc", "B. Dân chủ xã hội chủ nghĩa", "C. Dân chủ tư sản", "D. Dân chủ chủ nô"], 1,
     "Chế độ chính trị của nhà nước CHXHCN Việt Nam là dân chủ xã hội chủ nghĩa."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC3 - Câu 4",
     "Hình thức chính thể của nhà nước Việt Nam có đặc điểm gần với hình thức nào trong các phương án sau (theo đáp án bộ đề Quizizz)?",
     ["A. Cộng hòa tổng thống", "B. Cộng hòa lưỡng tính", "C. Cộng hòa đại nghị", "D. Chế độ độc đảng"], 2,
     "Theo đáp án gốc của đề PLDC3 (Câu 4) là Cộng hòa đại nghị (vì Quốc hội do dân bầu ra và Quốc hội bầu ra Chủ tịch nước, Chính phủ)."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC3 - Câu 5",
     "Chế độ chính trị phản dân chủ là gì?",
     ["A. Nhà nước độc tài", "B. Vi phạm các quyền tự do của nhân dân", "C. Vi phạm các quyền dân chủ của nhân dân", "D. Tất cả đều đúng"], 3,
     "Chế độ phản dân chủ mang tính độc tài, vi phạm quyền tự do và dân chủ của nhân dân."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC3 - Câu 9",
     "Hình thức cấu trúc nhà nước bao gồm những loại nào?",
     ["A. Nhà nước đơn nhất và nhà nước liên bang", "B. Chỉ có nhà nước đơn nhất", "C. Nhà nước đơn nhất, nhà nước liên bang và liên minh các nhà nước", "D. Chỉ có nhà nước liên bang"], 2,
     "Theo đáp án bộ đề PLDC3 (Câu 9), bao gồm nhà nước đơn nhất, nhà nước liên bang và liên minh các nhà nước."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC3 - Câu 10",
     "Nhà nước đơn nhất là nhà nước như thế nào?",
     ["A. Là nhà nước có chủ quyền chung, có lãnh thổ toàn vẹn, thống nhất; có một hệ thống các cơ quan nhà nước thống nhất từ trung ương đến địa phương; có một hệ thống pháp luật thống nhất trên toàn vẹn lãnh thổ quốc gia", "B. Là nhà nước có chủ quyền riêng ở từng vùng lãnh thổ", "C. Là nhà nước được thiết lập từ hai hay nhiều nhà nước thành viên", "D. Không có phương án nào đúng"], 0,
     "Nhà nước đơn nhất có 1 chủ quyền chung, 1 lãnh thổ thống nhất, 1 hệ thống cơ quan nhà nước và 1 hệ thống pháp luật thống nhất."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC3 - Câu 11",
     "Nhà nước liên bang là nhà nước như thế nào?",
     ["A. Là nhà nước được thiết lập từ hai hay nhiều nhà nước thành viên", "B. Là nhà nước được thiết lập từ hai hay nhiều vùng lãnh thổ", "C. Là nhà nước được thiết lập từ ba hay nhiều nhà nước thành viên", "D. Là nhà nước có một hệ thống pháp luật duy nhất"], 0,
     "Nhà nước liên bang được hợp thành từ hai hay nhiều nhà nước thành viên (bang)."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC3 - Câu 12",
     "Chế độ chính trị được hiểu là gì?",
     ["A. Là tổng thể các phương pháp để thực hiện quyền lực nhà nước", "B. Là tất cả các thiết chế chính trị trong xã hội", "C. Là toàn bộ đường lối chính sách mà đảng chính trị cầm quyền đề ra", "D. Tất cả đều đúng"], 0,
     "Chế độ chính trị là tổng thể các phương pháp, cách thức mà nhà nước sử dụng để thực hiện quyền lực nhà nước."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC3 - Câu 27 & PLDC8 - Câu 19",
     "Chính phủ có quyền ban hành những loại văn bản pháp luật nào (theo bộ đề Quizizz)?",
     ["A. Pháp lệnh, nghị quyết", "B. Nghị quyết, nghị định", "C. Luật, pháp lệnh", "D. Nghị quyết, nghị định, quyết định"], 1,
     "Theo đáp án gốc của bộ đề PLDC3 (Câu 27) và PLDC8 (Câu 19) là Nghị định, nghị quyết (Theo Luật Ban hành VBQPPL hiện hành, văn bản QPPL của Chính phủ là Nghị định)."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC3 - Câu 33",
     "Hoạt động nào sau đây thuộc chức năng của Viện kiểm sát nhân dân?",
     ["A. Hoạt động truy tố người phạm tội ra trước tòa án", "B. Hoạt động xét xử kẻ phạm tội", "C. Hoạt động thi hành án", "D. Cả ba hoạt động trên đều thuộc chức năng của Viện kiểm sát nhân dân"], 0,
     "Viện kiểm sát thực hiện quyền công tố (truy tố người phạm tội ra trước Tòa án) và kiểm sát hoạt động tư pháp."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC3 - Câu 34",
     "Cơ quan hành pháp là:",
     ["A. Chủ tịch nước, Chính phủ, Hội đồng nhân dân", "B. Quốc hội, Chính phủ", "C. Ủy ban thường vụ Quốc hội, Chủ tịch nước", "D. Tất cả đều sai"], 3,
     "Cơ quan hành pháp là Chính phủ và UBND các cấp. Các phương án A, B, C đều ghép thêm cơ quan lập pháp hoặc nguyên thủ quốc gia nên đều sai."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC4 - Câu 1",
     "Viện kiểm sát nằm trong hệ thống cơ quan nào của bộ máy nhà nước Việt Nam?",
     ["A. Hành pháp", "B. Tư pháp", "C. Lập pháp", "D. Tòa án"], 1,
     "Viện kiểm sát nhân dân thuộc hệ thống cơ quan tư pháp."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC4 - Câu 2",
     "Căn cứ vào phạm vi hoạt động của nhà nước, chức năng của nhà nước được phân thành:",
     ["A. Chức năng đối nội", "B. Chức năng đối ngoại", "C. Đáp án A và B đều đúng", "D. Không có đáp án nào đúng"], 2,
     "Theo phạm vi lãnh thổ/hoạt động, chức năng nhà nước chia thành chức năng đối nội và chức năng đối ngoại."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC4 - Câu 4",
     "Hệ thống chính trị Việt Nam gồm mấy bộ phận (mấy chủ thể)?",
     ["A. 5", "B. 4", "C. 3", "D. 2"], 2,
     "Hệ thống chính trị Việt Nam gồm 3 bộ phận cấu thành: Đảng Cộng sản Việt Nam, Nhà nước CHXHCN Việt Nam, Mặt trận Tổ quốc Việt Nam và các tổ chức chính trị - xã hội."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC4 - Câu 5",
     "Trung tâm của bộ máy nhà nước Cộng hòa xã hội chủ nghĩa Việt Nam là cơ quan nào?",
     ["A. Quốc hội", "B. Ủy ban nhân dân các cấp", "C. Hội đồng nhân dân các cấp", "D. Chính phủ"], 0,
     "Quốc hội là cơ quan quyền lực nhà nước cao nhất, giữ vị trí trung tâm của Bộ máy nhà nước (còn trung tâm của Hệ thống chính trị là Nhà nước)."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC4 - Câu 6 & PLDC8 - Câu 28",
     "Nguyên thủ quốc gia của nước Cộng hòa XHCN Việt Nam là:",
     ["A. Chủ tịch Quốc hội", "B. Chủ tịch nước", "C. Thủ tướng Chính phủ", "D. Tổng Bí thư"], 1,
     "Chủ tịch nước là người đứng đầu Nhà nước (Nguyên thủ quốc gia), thay mặt nước CHXHCN Việt Nam về đối nội và đối ngoại."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC7 - Câu 29",
     "Nhà nước CHXHCN Việt Nam có hình thức cấu trúc:",
     ["A. Nhà nước đơn nhất", "B. Liên bang", "C. Liên minh", "D. Quân chủ lập hiến"], 0,
     "Việt Nam là nhà nước đơn nhất."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC8 - Câu 7",
     "Nhà nước Việt Nam đại diện cho lợi ích của những giai cấp nào?",
     ["A. Nhân dân lao động", "B. Giai cấp công nhân", "C. Các tầng lớp bị áp bức", "D. Giai cấp công nhân và nhân dân lao động"], 3,
     "Nhà nước CHXHCN Việt Nam mang bản chất giai cấp công nhân, đại diện cho lợi ích của giai cấp công nhân và nhân dân lao động."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC8 - Câu 14",
     "Ủy ban Thường vụ Quốc hội ban hành những văn bản quy phạm pháp luật nào?",
     ["A. Pháp lệnh, nghị quyết", "B. Nghị quyết", "C. Pháp lệnh", "D. Nghị định"], 0,
     "Ủy ban Thường vụ Quốc hội ban hành Pháp lệnh và Nghị quyết."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC8 - Câu 16",
     "Văn bản nào sau đây KHÔNG phải là văn bản quy phạm pháp luật?",
     ["A. Thông tư của Bộ trưởng", "B. Luật, bộ luật của Quốc hội", "C. Chỉ thị của Thủ tướng", "D. Lệnh của Chủ tịch nước"], 2,
     "Theo Luật Ban hành VBQPPL, Chỉ thị của Thủ tướng Chính phủ là văn bản hành chính thông thường, không phải là VBQPPL (Thủ tướng ban hành Quyết định)."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC8 - Câu 17",
     "Bộ trưởng được ban hành văn bản quy phạm pháp luật nào sau đây?",
     ["A. Thông tư", "B. Nghị quyết", "C. Nghị định", "D. Luật giáo dục đại học"], 0,
     "Bộ trưởng, Thủ trưởng cơ quan ngang bộ ban hành Thông tư."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC8 - Câu 18",
     "Pháp lệnh là văn bản do cơ quan nào ban hành?",
     ["A. Quốc hội", "B. Chính phủ", "C. Ủy ban Thường vụ Quốc hội", "D. Cả ba phương án đều đúng"], 2,
     "Pháp lệnh thuộc thẩm quyền ban hành của Ủy ban Thường vụ Quốc hội."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC9 - Câu 13",
     "Bộ phận tạo thành bộ máy nhà nước là:",
     ["A. Cơ quan nhà nước", "B. Cơ quan luật pháp", "C. Cơ quan hành pháp", "D. Cả B và C đều đúng"], 0,
     "Phần tử cấu thành nên bộ máy nhà nước là các cơ quan nhà nước."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC9 - Câu 14",
     "Hệ thống cơ quan trong bộ máy nhà nước bao gồm mấy hệ thống?",
     ["A. Cơ quan lập pháp", "B. Cơ quan hành pháp", "C. Cơ quan tư pháp", "D. Cả ba hệ thống nêu trên"], 3,
     "Hệ thống cơ quan trong bộ máy nhà nước gồm các cơ quan lập pháp, hành pháp và tư pháp."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC9 - Câu 16",
     "Tòa án thuộc hệ thống cơ quan nào trong nhà nước?",
     ["A. Tư pháp", "B. Hành pháp", "C. Lập pháp", "D. Cả ba hệ thống nêu trên"], 0,
     "Tòa án là cơ quan xét xử, thực hiện quyền tư pháp."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC9 - Câu 17",
     "Ủy ban nhân dân các cấp nằm trong hệ thống cơ quan nào trong bộ máy nhà nước?",
     ["A. Cơ quan hành chính", "B. Cơ quan đại diện nhân dân", "C. Cơ quan lập pháp", "D. Cơ quan xét xử"], 0,
     "Ủy ban nhân dân các cấp là cơ quan hành chính nhà nước ở địa phương."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC9 - Câu 18",
     "Chính phủ là cơ quan nhà nước:",
     ["A. Cơ quan không do người dân trực tiếp bầu ra", "B. Người dân trực tiếp bầu ra", "C. Việc thành lập bởi nguyên thủ quốc gia", "D. Tòa án bầu ra"], 0,
     "Chính phủ không do cử tri trực tiếp bầu mà do Quốc hội thành lập."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC9 - Câu 19",
     "Nguyên thủ quốc gia trong chính thể cộng hòa đại nghị do ai bầu ra?",
     ["A. Do người dân cả nước bầu ra", "B. Do nghị viện (quốc hội) bầu ra", "C. Do nhân dân địa phương bầu ra", "D. Tất cả các đáp án trên đều đúng"], 1,
     "Trong chính thể cộng hòa đại nghị, nguyên thủ quốc gia do Nghị viện (Quốc hội) bầu ra."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC9 - Câu 20",
     "Các Bộ là cơ quan nhà nước thuộc:",
     ["A. Ủy ban nhân dân", "B. Quốc hội", "C. Chính phủ", "D. Tòa án"], 2,
     "Các Bộ và cơ quan ngang Bộ là cơ quan của Chính phủ."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC9 - Câu 21",
     "Tổ chức bộ máy nhà nước XHCN nói chung, bộ máy nhà nước CHXHCN Việt Nam nói riêng tuân theo nguyên tắc gì?",
     ["A. Quyền lực nhà nước được giao cho các cơ quan độc lập đảm nhiệm", "B. Quyền lực nhà nước thống nhất, tất cả quyền lực nhà nước thuộc về nhân dân", "C. A và B đều sai", "D. Tất cả đều đúng"], 1,
     "Quyền lực nhà nước là thống nhất, có sự phân công, phối hợp, kiểm soát giữa các cơ quan, tất cả quyền lực thuộc về nhân dân."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC9 - Câu 22",
     "Trong bộ máy nhà nước Cộng hòa xã hội chủ nghĩa Việt Nam, Hội đồng nhân dân các cấp là:",
     ["A. Cơ quan của Quốc hội ở địa phương", "B. Cơ quan kiêm nhiệm ở địa phương", "C. Cơ quan lập pháp", "D. Cơ quan đại diện quyền lực cao nhất ở địa phương"], 3,
     "HĐND là cơ quan quyền lực nhà nước ở địa phương, đại diện cho ý chí, nguyện vọng và quyền làm chủ của nhân dân địa phương."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC9 - Câu 23",
     "Khi quy định mỗi cơ quan nhà nước có một thẩm quyền nhất định có nghĩa là:",
     ["A. Cơ quan nhà nước có quyền làm những công việc không thuộc nhiệm vụ của mình", "B. Cơ quan nhà nước được sử dụng quyền lực nhà nước ở bất kỳ công việc nào", "C. Cơ quan nhà nước chỉ được làm những gì mà pháp luật quy định", "D. Cơ quan nhà nước không được nhân danh nhà nước khi làm nhiệm vụ"], 2,
     "Cơ quan nhà nước, cán bộ, công chức nhà nước chỉ được làm những gì pháp luật cho phép/quy định."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC9 - Câu 24",
     "Khi thực hiện chức năng xét xử, Tòa án nhân danh ai để xét xử?",
     ["A. Cơ quan có thẩm quyền", "B. Quốc hội", "C. Nhà nước", "D. Ủy ban nhân dân"], 2,
     "Tòa án nhân dân xét xử và tuyên án nhân danh Nước Cộng hòa xã hội chủ nghĩa Việt Nam."),

    ("2. Hệ thống chính trị & Bộ máy Nhà nước VN", "PLDC9 - Câu 25",
     "Bộ máy nhà nước Việt Nam được thành lập ở mấy cấp (theo bộ đề Quizizz)?",
     ["A. 4 cấp", "B. 2 cấp", "C. 3 cấp", "D. 1 cấp"], 0,
     "Theo đáp án bộ đề PLDC9 (Câu 25) là 4 cấp (Trung ương, Cấp tỉnh, Cấp huyện, Cấp xã)."),

    # =========================================================================
    # PHẦN 3: NHẬP MÔN, BẢN CHẤT, THUỘC TÍNH, CHỨC NĂNG & NGUỒN CỦA PHÁP LUẬT
    # =========================================================================
    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC1 - Câu 1 & PLDC6 - Câu 25",
     "Pháp luật đại cương nằm trong tiểu hệ thống nào?",
     ["A. Khoa học pháp lý cơ bản", "B. Khoa học pháp lý chuyên ngành, liên ngành", "C. Khoa học pháp lý quốc tế", "D. Khoa học pháp lý ứng dụng kỹ thuật"], 0,
     "Pháp luật đại cương thuộc nhóm các ngành khoa học pháp lý cơ bản."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC1 - Câu 16",
     "Nguồn sớm nhất hình thành pháp luật là:",
     ["A. Tiền lệ pháp", "B. Tập quán pháp", "C. Văn bản pháp luật", "D. Các học thuyết chính trị - pháp lý"], 1,
     "Tập quán pháp là hình thức (nguồn) pháp luật cổ xưa và sớm nhất trong lịch sử."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC1 - Câu 17",
     "Học thuyết pháp luật tự nhiên cho rằng:",
     ["A. Pháp luật xuất phát từ cuộc sống tự nhiên hoang dã", "B. Pháp luật là tổng thể các quyền và nghĩa vụ của con người tự nhiên sinh ra đã có", "C. Pháp luật là hệ thống quy tắc của tự nhiên", "D. Cả 03 phương án trên đều đúng"], 1,
     "Thuyết pháp luật tự nhiên cho rằng các quyền con người là bẩm sinh, tự nhiên sinh ra đã có."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC1 - Câu 18",
     "Các nguyên tắc của pháp luật là yếu tố quan trọng thuộc:",
     ["A. Hình thức bên trong của pháp luật", "B. Hình thức bên ngoài của pháp luật", "C. Cấu trúc của văn bản pháp luật", "D. Cả 03 phương án trên đều đúng"], 0,
     "Các nguyên tắc pháp luật thuộc về hình thức bên trong (cấu trúc nội dung) của pháp luật."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC1 - Câu 19 & PLDC7 - Câu 26",
     "Việc Tòa án nhân dân thường đưa các vụ án đi xét xử lưu động thể hiện chủ yếu chức năng nào của pháp luật?",
     ["A. Chức năng điều chỉnh các quan hệ xã hội", "B. Chức năng bảo vệ các quan hệ xã hội", "C. Chức năng giáo dục pháp luật", "D. Tất cả các phương án trên đều sai"], 2,
     "Xét xử lưu động nhằm tuyên truyền, nâng cao ý thức pháp luật cho người dân, thể hiện chủ yếu chức năng giáo dục."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC1 - Câu 20 & PLDC6 - Câu 5",
     "\"Nội dung của pháp luật phải được quy định rõ ràng, chặt chẽ trong các văn bản pháp luật\" là biểu hiện thuộc tính nào của pháp luật?",
     ["A. Tính quy phạm phổ biến", "B. Tính xác định chặt chẽ về mặt hình thức", "C. Tính bắt buộc chung", "D. Tính cưỡng chế nhà nước"], 1,
     "Ngôn ngữ rõ ràng, chính xác, một nghĩa trong văn bản là biểu hiện của tính xác định chặt chẽ về mặt hình thức."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC1 - Câu 34",
     "Các hệ thống pháp luật phổ biến trên thế giới được phân loại thành mấy nhóm (theo đáp án bộ đề PLDC1)?",
     ["A. 02 nhóm", "B. 03 nhóm", "C. 04 nhóm", "D. 05 nhóm"], 1,
     "Theo đáp án gốc của bộ đề PLDC1 (Câu 34) là 03 nhóm chính (Civil Law, Common Law, Islamic Law/XHCN)."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC2 - Câu 1",
     "Pháp luật đại cương nghiên cứu những vấn đề cơ bản về cái gì?",
     ["A. Pháp luật", "B. Nhà nước", "C. Kinh tế chính trị pháp luật", "D. Nhà nước và pháp luật"], 3,
     "Pháp luật đại cương nghiên cứu những vấn đề cơ bản nhất về cả Nhà nước và Pháp luật."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC2 - Câu 2",
     "Nội dung của môn học Pháp luật đại cương bao gồm:",
     ["A. Các ngành luật chính trong hệ thống pháp luật Việt Nam", "B. Các hệ thống pháp luật trên thế giới", "C. Những vấn đề cơ bản về nhà nước và pháp luật", "D. Cả ba đáp án trên"], 3,
     "Nội dung môn học bao quát cả lý luận chung về nhà nước và pháp luật, các hệ thống pháp luật thế giới và các ngành luật chính của Việt Nam."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC2 - Câu 3",
     "Pháp luật đại cương là ngành khoa học thuộc:",
     ["A. Khoa học kỹ thuật", "B. Khoa học xã hội", "C. Khoa học chính trị", "D. Khoa học pháp lý"], 3,
     "Pháp luật đại cương thuộc ngành khoa học pháp lý."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC2 - Câu 4",
     "Mối quan hệ giữa nhà nước và pháp luật là?",
     ["A. Quan hệ một chiều", "B. Quan hệ qua lại ràng buộc tác động lẫn nhau", "C. Không có quan hệ gì", "D. Quan hệ phụ thuộc tuyệt đối một bên"], 1,
     "Nhà nước và pháp luật có mối quan hệ hữu cơ, tác động qua lại và ràng buộc lẫn nhau."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC2 - Câu 24",
     "Pháp luật là một hiện tượng:",
     ["A. Chỉ mang tính xã hội không mang tính giai cấp", "B. Chỉ mang tính giai cấp không mang tính xã hội", "C. Cả ba đáp án trên đều sai", "D. Vừa mang tính xã hội vừa mang tính giai cấp"], 3,
     "Tương tự như Nhà nước, Pháp luật vừa mang bản chất giai cấp vừa mang bản chất xã hội."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC2 - Câu 25",
     "Pháp luật thể hiện ý chí của giai cấp thống trị là:",
     ["A. Thuộc tính cơ bản của pháp luật", "B. Nguồn của pháp luật", "C. Bản chất xã hội của pháp luật", "D. Bản chất giai cấp của pháp luật"], 3,
     "Pháp luật phản ánh ý chí của giai cấp thống trị được đề lên thành luật, đó là bản chất giai cấp."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC2 - Câu 26",
     "Tính giai cấp của pháp luật thể hiện ở nhận định nào?",
     ["A. Pháp luật là ý chí của giai cấp thống trị", "B. Pháp luật là sản phẩm của xã hội có giai cấp", "C. Pháp luật là công cụ điều chỉnh các mối quan hệ giai cấp", "D. Cả ba đáp án trên"], 3,
     "Cả 3 nhận định trên đều phản ánh tính giai cấp của pháp luật."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC2 - Câu 27",
     "Pháp luật mang bản chất xã hội vì:",
     ["A. Phù hợp với ý chí của giai cấp cầm quyền", "B. Phù hợp với ý chí của giai cấp bị trị", "C. Ghi nhận và bảo vệ lợi ích của các giai cấp và tầng lớp trong xã hội", "D. Cả B và C"], 3,
     "Theo đáp án gốc của bộ đề PLDC2 (Câu 27) là Cả B và C."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC2 - Câu 28",
     "Tính cưỡng chế của pháp luật được thể hiện ở chỗ:",
     ["A. Những hành vi vi phạm pháp luật đều bị áp dụng hình phạt", "B. Những hành vi vi phạm pháp luật đều bị xử lý kỷ luật", "C. Những hành vi vi phạm pháp luật đều có thể bị áp dụng các biện pháp chế tài", "D. Những hành vi vi phạm pháp luật đều bị xử phạt hành chính"], 2,
     "Hình phạt, kỷ luật hay phạt hành chính chỉ là một loại chế tài cụ thể; khái quát nhất là bị áp dụng các biện pháp chế tài."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC2 - Câu 29 & PLDC7 - Câu 27",
     "Tính quy phạm phổ biến và bắt buộc chung của pháp luật là:",
     ["A. Chức năng của pháp luật", "B. Hình thức của pháp luật", "C. Bản chất của pháp luật", "D. Thuộc tính của pháp luật"], 3,
     "Tính quy phạm phổ biến, tính xác định chặt chẽ về hình thức và tính được đảm bảo thực hiện bởi nhà nước là 3 thuộc tính của pháp luật."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC2 - Câu 30",
     "Ngôn ngữ pháp lý rõ ràng và chính xác thể hiện thuộc tính nào của pháp luật?",
     ["A. Tính bắt buộc chung", "B. Tính xác định chặt chẽ về mặt hình thức", "C. Tính quy phạm phổ biến", "D. Không có đáp án đúng"], 1,
     "Ngôn ngữ rõ ràng, chính xác thể hiện tính xác định chặt chẽ về mặt hình thức."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC2 - Câu 31",
     "Pháp luật được nhà nước đảm bảo thực hiện bằng biện pháp chủ yếu gì?",
     ["A. Cả ba đáp án trên", "B. Thỏa thuận", "C. Cưỡng chế", "D. Tự nguyện"], 2,
     "Khác với đạo đức hay tập quán, pháp luật được Nhà nước đảm bảo thực hiện bằng sức mạnh cưỡng chế."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC2 - Câu 32",
     "Pháp luật có khả năng điều chỉnh hành vi của con người là:",
     ["A. Cả ba đáp án trên", "B. Chức năng của pháp luật", "C. Thuộc tính của pháp luật", "D. Bản chất của pháp luật"], 1,
     "Điều chỉnh hành vi con người và các quan hệ xã hội là chức năng của pháp luật."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC2 - Câu 33",
     "Pháp luật có mấy chức năng cơ bản?",
     ["A. 2", "B. 1", "C. 3", "D. 4"], 2,
     "Pháp luật có 3 chức năng cơ bản: Chức năng điều chỉnh, chức năng bảo vệ và chức năng giáo dục."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC2 - Câu 34 & PLDC7 - Câu 28",
     "Chức năng điều chỉnh của pháp luật có nghĩa là:",
     ["A. Pháp luật tác động tới hành vi của con người", "B. Pháp luật tác động tới ý thức và tâm lý của con người", "C. Pháp luật quy định các phương tiện nhằm mục đích bảo vệ các quan hệ xã hội", "D. Cả A và B"], 0,
     "Chức năng điều chỉnh là sự tác động của pháp luật tới hành vi của con người (còn tác động tới ý thức và tâm lý là chức năng giáo dục)."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC2 - Câu 35",
     "Chức năng giáo dục của pháp luật có nghĩa là:",
     ["A. Pháp luật tác động tới hành vi của con người", "B. Pháp luật tác động tới ý thức và tâm lý của con người", "C. Pháp luật quy định các phương tiện nhằm mục đích bảo vệ các quan hệ xã hội", "D. Cả A và B"], 1,
     "Chức năng giáo dục thể hiện qua việc pháp luật tác động vào ý thức, tâm lý của con người, giúp hình thành thói quen xử sự hợp pháp."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC5 - Câu 17",
     "Hệ thống pháp luật Islamic Law còn được gọi là:",
     ["A. Hệ thống pháp luật dân luật", "B. Hệ thống pháp luật thông luật", "C. Hệ thống pháp luật Hồi giáo", "D. Cả 3 đáp án đều sai"], 2,
     "Islamic Law là hệ thống pháp luật Hồi giáo."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC5 - Câu 18",
     "Điều kiện để xác định một quốc gia thuộc hệ thống pháp luật Islamic Law là:",
     ["A. Đạo Hồi là quốc đạo của quốc gia", "B. Quốc gia lấy quy định trong kinh thánh của Đạo Hồi làm luật", "C. A và B đúng", "D. Đạo Hồi được coi là một tôn giáo thông thường của quốc gia đó"], 2,
     "Quốc gia thuộc hệ thống luật Hồi giáo khi coi Đạo Hồi là quốc đạo và lấy quy định trong Kinh Koran làm luật."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC6 - Câu 1",
     "Pháp luật có tính quy phạm phổ biến có nghĩa là:",
     ["A. Các quy phạm pháp luật được áp dụng một lần duy nhất", "B. Quy phạm pháp luật được áp dụng nhiều lần", "C. Quy phạm pháp luật được khái quát hóa từ nhiều trường hợp mang tính phổ biến trong xã hội", "D. Cả B và C"], 3,
     "Tính quy phạm phổ biến thể hiện ở việc quy phạm là khuôn mẫu chung được khái quát hóa từ các trường hợp phổ biến và được áp dụng lặp đi lặp lại nhiều lần."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC6 - Câu 2",
     "Khi nghiên cứu về bản chất của pháp luật thì khẳng định nào sau đây là SAI?",
     ["A. Pháp luật vừa mang tính chủ quan lại vừa mang tính khách quan", "B. Pháp luật bao giờ cũng thể hiện bản chất giai cấp rõ nét hơn bản chất xã hội", "C. Pháp luật là ý chí của giai cấp thống trị được đề lên thành luật", "D. Pháp luật là hiện tượng vừa mang tính giai cấp vừa mang tính xã hội"], 1,
     "Tùy từng kiểu pháp luật và giai đoạn lịch sử mà tính giai cấp hay tính xã hội nổi trội hơn, không phải bao giờ tính giai cấp cũng rõ nét hơn."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC6 - Câu 3",
     "Chọn phương án đúng nhất để điền vào chỗ trống: \"Xuất phát từ ... cho nên bất cứ nhà nước nào cũng dùng pháp luật làm phương tiện chủ yếu để quản lý mọi mặt đời sống xã hội\".",
     ["A. Tính cưỡng chế của pháp luật", "B. Những thuộc tính cơ bản của pháp luật", "C. Tính xác định chặt chẽ về mặt hình thức của pháp luật", "D. Tính quy phạm phổ biến của pháp luật"], 1,
     "Nhờ tổng thể những thuộc tính cơ bản ưu việt của pháp luật mà mọi nhà nước đều dùng pháp luật làm công cụ quản lý chủ yếu."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC6 - Câu 4",
     "Đáp án nào sau đây thể hiện thuộc tính của pháp luật?",
     ["A. Tính chính xác", "B. Tính quy phạm phổ biến và bắt buộc chung", "C. Tính minh bạch", "D. Tất cả đều đúng"], 1,
     "Tính quy phạm phổ biến (và bắt buộc chung) là thuộc tính cơ bản của pháp luật."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC6 - Câu 6",
     "Pháp luật chủ nô quy định:",
     ["A. Quyền lực của mọi người trong xã hội là như nhau", "B. Công khai quyền lực vô hạn của chủ nô", "C. Tình trạng vô quyền của giai cấp nô lệ", "D. Cả B và C"], 3,
     "Pháp luật chủ nô công khai bảo vệ quyền lực vô hạn của chủ nô và sự vô quyền của nô lệ (coi nô lệ là tài sản biết nói)."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC6 - Câu 7",
     "Khẳng định nào sau đây KHÔNG đúng về pháp luật chủ nô (theo đáp án bộ đề PLDC6)?",
     ["A. Công khai bảo vệ quyền tư hữu của chủ nô", "B. Củng cố tình trạng bất bình đẳng trong xã hội", "C. Là kiểu pháp luật đầu tiên trong lịch sử", "D. Mang nặng dấu ấn tôn giáo"], 3,
     "Theo đáp án gốc của bộ đề PLDC6 (Câu 7 và Câu 12), 'Mang nặng dấu ấn tôn giáo' được xếp là đặc điểm điển hình của pháp luật phong kiến."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC6 - Câu 8",
     "Đặc điểm của pháp luật phong kiến là gì?",
     ["A. Mang nặng dấu ấn tôn giáo", "B. Quy định những hình phạt rất tàn bạo", "C. Bảo vệ chế độ tư hữu của giai cấp thống trị", "D. Cả ba đáp án trên"], 3,
     "Pháp luật phong kiến bảo vệ chế độ tư hữu địa chủ, mang nặng dấu ấn tôn giáo và quy định nhiều hình phạt hà khắc, tàn bạo."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC6 - Câu 9",
     "Kiểu pháp luật phong kiến thể hiện ý chí của:",
     ["A. Giai cấp thống trị", "B. Giai cấp địa chủ", "C. Giai cấp phong kiến", "D. Cả ba câu trên đều đúng"], 3,
     "Trong xã hội phong kiến, giai cấp thống trị chính là giai cấp địa chủ / phong kiến."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC6 - Câu 10",
     "Hình thức phổ biến nhất của pháp luật chủ nô là:",
     ["A. Tín điều tôn giáo", "B. Văn bản pháp luật", "C. Tập quán pháp", "D. Tiền lệ pháp"], 2,
     "Hình thức phổ biến nhất của pháp luật chủ nô là tập quán pháp."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC6 - Câu 11",
     "Pháp luật chủ nô cho phép chủ nô có quyền chiếm hữu đối với:",
     ["A. Tài sản", "B. Tư liệu sản xuất", "C. Nô lệ", "D. Cả ba đáp án trên"], 3,
     "Chủ nô có quyền sở hữu tuyệt đối với tài sản, tư liệu sản xuất và cả người nô lệ."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC6 - Câu 12",
     "Kiểu pháp luật nào chịu ảnh hưởng mạnh mẽ của tôn giáo?",
     ["A. Pháp luật xã hội chủ nghĩa", "B. Pháp luật tư sản", "C. Pháp luật phong kiến", "D. Pháp luật chủ nô"], 2,
     "Theo đáp án gốc của bộ đề PLDC6 (Câu 12), pháp luật phong kiến chịu ảnh hưởng mạnh mẽ của tôn giáo và đạo đức phong kiến."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC6 - Câu 13",
     "Nguồn luật chủ yếu của hệ thống Common Law là gì?",
     ["A. Lẽ phải", "B. Án lệ (Tiền lệ pháp)", "C. Văn bản pháp luật", "D. Tập quán pháp"], 1,
     "Hệ thống Common Law (Thông luật / Anh - Mỹ) coi Án lệ là nguồn luật chủ yếu."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC6 - Câu 14",
     "Hình thức tố tụng được dùng chủ yếu trong hệ thống Common Law là hình thức nào?",
     ["A. Tranh tụng tại tòa", "B. Tranh tụng hành chính", "C. Tranh tụng hình sự", "D. Tranh tụng dân sự"], 0,
     "Hệ thống Common Law áp dụng mô hình tố tụng tranh tụng tại tòa."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC6 - Câu 26",
     "Đặc điểm nào sau đây là dấu hiệu đặc trưng của nhà nước?",
     ["A. Nhà nước ban hành pháp luật và đảm bảo thực hiện pháp luật", "B. Nhà nước chỉ tồn tại trong xã hội có giai cấp", "C. Nhà nước ra đời khi có sự xuất hiện chế độ tư hữu", "D. Nhà nước luôn mang bản chất giai cấp và bản chất xã hội"], 0,
     "Ban hành pháp luật và quản lý xã hội bằng pháp luật là một trong 5 dấu hiệu đặc trưng của Nhà nước."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC7 - Câu 1 & Câu 30",
     "Khẳng định nào là đúng về nguồn (hình thức) của pháp luật?",
     ["A. Nguồn của pháp luật nói chung chỉ là văn bản quy phạm pháp luật", "B. Nguồn của pháp luật nói chung là văn bản quy phạm pháp luật và tập quán pháp", "C. Nguồn của pháp luật nói chung là văn bản quy phạm pháp luật, tập quán pháp và tiền lệ pháp", "D. Cả A, B và C đều sai"], 2,
     "Ba hình thức (nguồn) cơ bản của pháp luật là: Văn bản quy phạm pháp luật, tập quán pháp và tiền lệ pháp (án lệ)."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC7 - Câu 7",
     "Tính xác định chặt chẽ về mặt hình thức là thuộc tính của:",
     ["A. Tôn giáo", "B. Pháp luật", "C. Đạo đức", "D. Tập quán"], 1,
     "Chỉ có pháp luật mới có thuộc tính xác định chặt chẽ về mặt hình thức."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC7 - Câu 8",
     "Nguồn chủ yếu của hệ thống pháp luật Việt Nam là:",
     ["A. Tập quán pháp", "B. Tiền lệ tư pháp", "C. Tiền lệ pháp", "D. Văn bản quy phạm pháp luật"], 3,
     "Ở Việt Nam, văn bản quy phạm pháp luật là nguồn chủ yếu và quan trọng nhất."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC7 - Câu 16",
     "Dòng họ Civil Law còn có tên gọi khác là gì?",
     ["A. Hệ thống pháp luật Anh - Mỹ", "B. Hệ thống pháp luật Châu Mỹ Lục địa", "C. Hệ thống pháp luật Châu Âu Lục địa", "D. Hệ thống pháp luật Hồi Giáo"], 2,
     "Civil Law (Dân luật) còn gọi là Hệ thống pháp luật Châu Âu lục địa (Pháp - Đức)."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC7 - Câu 17",
     "Nguồn chủ yếu của hệ thống pháp luật Civil Law là:",
     ["A. Luật thành văn (Văn bản quy phạm pháp luật)", "B. Các học thuyết pháp lý", "C. Tập quán pháp", "D. Án lệ"], 0,
     "Hệ thống Civil Law coi trọng luật thành văn (văn bản quy phạm pháp luật, đặc biệt là các Bộ luật) làm nguồn chủ yếu."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC8 - Câu 2",
     "Chọn nhận định đúng nhất thể hiện mối quan hệ giữa nhà nước và pháp luật:",
     ["A. Nhà nước xây dựng và thực hiện pháp luật nên nó có thể đứng trên pháp luật", "B. Pháp luật là phương tiện quản lý của nhà nước nhưng nhà nước không cần tuân theo", "C. Pháp luật có trước nhà nước", "D. Nhà nước ban hành pháp luật và quản lý bằng pháp luật nhưng bị ràng buộc bởi pháp luật"], 3,
     "Nhà nước ban hành pháp luật để quản lý xã hội nhưng chính nhà nước cũng phải tôn trọng và bị ràng buộc bởi pháp luật."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC8 - Câu 8",
     "Pháp luật do Nhà nước ban hành có đặc điểm gì?",
     ["A. Nhà nước tôn trọng và thực hiện pháp luật", "B. Có tính bắt buộc chung", "C. Mọi công dân đều phải tôn trọng và thực hiện theo pháp luật", "D. Cả ba phương án còn lại đều đúng"], 3,
     "Pháp luật có tính bắt buộc chung đối với mọi công dân và cả chính Nhà nước."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC8 - Câu 20",
     "Tập quán pháp là gì?",
     ["A. Tập quán được lưu truyền trong xã hội", "B. Phù hợp với lợi ích của nhà nước và thực tiễn cuộc sống", "C. Tập quán được nhà nước thừa nhận trở thành pháp luật", "D. Cả A, B và C"], 3,
     "Tập quán pháp là những tập quán lưu truyền trong xã hội, phù hợp với lợi ích của giai cấp thống trị/nhà nước và được nhà nước thừa nhận nâng lên thành pháp luật."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC8 - Câu 21",
     "Tiền lệ pháp (án lệ) là gì?",
     ["A. Là việc nhà nước thừa nhận những bản án, quyết định của cơ quan hành chính, của tòa án khi giải quyết những vụ việc cụ thể để áp dụng cho những vụ việc tương tự về sau", "B. Là mọi văn bản do Quốc hội ban hành", "C. Là những phong tục tập quán lâu đời", "D. Là các điều ước quốc tế"], 0,
     "Tiền lệ pháp là việc nhà nước thừa nhận các bản án, quyết định giải quyết vụ việc cụ thể làm khuôn mẫu để giải quyết các vụ việc tương tự về sau."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC8 - Câu 24",
     "Khẳng định nào sau đây là đúng?",
     ["A. Chỉ có nhà nước mới có quyền ban hành pháp luật", "B. Không chỉ có nhà nước mà các tổ chức xã hội cũng có quyền ban hành pháp luật", "C. Mọi cá nhân đều có quyền ban hành pháp luật", "D. Cả B và C"], 0,
     "Nhà nước là chủ thể duy nhất có quyền ban hành pháp luật."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC8 - Câu 26",
     "Bản chất của pháp luật bao gồm:",
     ["A. Tính giai cấp và tính xã hội", "B. Tính giáo dục, thuyết phục và cưỡng chế", "C. Tính quy phạm và bắt buộc chung", "D. Cả 3 phương án trên"], 0,
     "Bản chất của pháp luật gồm 2 mặt: tính giai cấp và tính xã hội."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC9 - Câu 4",
     "Khi nghiên cứu về nhà nước và pháp luật thì nó gắn liền với phương pháp nghiên cứu nền tảng nào?",
     ["A. Trực quan sinh động", "B. Duy vật lịch sử", "C. Duy vật biện chứng", "D. Duy vật biện chứng và duy vật lịch sử"], 3,
     "Phương pháp luận nghiên cứu nhà nước và pháp luật dựa trên chủ nghĩa duy vật biện chứng và duy vật lịch sử."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC9 - Câu 5",
     "Môn học Pháp luật đại cương thuộc lĩnh vực nào của khoa học xã hội?",
     ["A. Khoa học kinh tế", "B. Khoa học văn hóa", "C. Khoa học tâm lý", "D. Khoa học chính trị - pháp lý"], 3,
     "Pháp luật đại cương thuộc lĩnh vực khoa học chính trị - pháp lý."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC9 - Câu 6",
     "Trong lĩnh vực nghiên cứu khoa học pháp lý, pháp luật đại cương là:",
     ["A. Nghiên cứu những vấn đề nền tảng cốt lõi của nhà nước và pháp luật", "B. Nghiên cứu về một nhà nước cụ thể", "C. Nghiên cứu về một kiểu nhà nước, kiểu pháp luật cụ thể", "D. Nghiên cứu chuyên sâu về một ngành luật duy nhất"], 0,
     "Pháp luật đại cương nghiên cứu những vấn đề nền tảng cốt lõi nhất về nhà nước và pháp luật."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC9 - Câu 7",
     "Khi nghiên cứu về pháp luật đại cương liên quan tới các lĩnh vực xã hội nào?",
     ["A. Lĩnh vực về tư tưởng", "B. Lĩnh vực về kinh tế", "C. Lĩnh vực về văn hóa", "D. Tất cả các lĩnh vực đã nêu"], 3,
     "Nhà nước và pháp luật gắn liền với mọi mặt đời sống: kinh tế, tư tưởng, văn hóa, xã hội."),

    ("3. Nhập môn, Bản chất, Thuộc tính, Chức năng & Nguồn PL", "PLDC9 - Câu 26",
     "Chức năng nào sau đây KHÔNG phải là chức năng của pháp luật?",
     ["A. Chức năng giáo dục", "B. Chức năng điều chỉnh các quan hệ xã hội", "C. Chức năng bảo vệ các quan hệ xã hội", "D. Chức năng xây dựng các quan hệ xã hội"], 3,
     "Pháp luật có 3 chức năng: điều chỉnh, bảo vệ, giáo dục. Không có 'chức năng xây dựng các quan hệ xã hội'."),

    # =========================================================================
    # PHẦN 4: QUY PHẠM PHÁP LUẬT, HỆ THỐNG PHÁP LUẬT & VĂN BẢN QPPL
    # =========================================================================
    ("4. Quy phạm PL, Hệ thống PL & Văn bản QPPL", "PLDC1 - Câu 21 & PLDC8 - Câu 11",
     "Trong hệ thống pháp luật Việt Nam, để được coi là một ngành luật độc lập khi:",
     ["A. Ngành luật đó phải có đối tượng điều chỉnh riêng", "B. Ngành luật đó phải có phương pháp điều chỉnh riêng", "C. Ngành luật đó phải có đầy đủ các VBQPPL", "D. Ngành luật đó phải có cả đối tượng điều chỉnh và phương pháp điều chỉnh"], 3,
     "Hai tiêu chí căn bản để phân định một ngành luật độc lập là đối tượng điều chỉnh và phương pháp điều chỉnh."),

    ("4. Quy phạm PL, Hệ thống PL & Văn bản QPPL", "PLDC1 - Câu 23 & PLDC8 - Câu 22",
     "Văn bản quy phạm pháp luật được áp dụng từ thời điểm nào?",
     ["A. Bắt đầu có hiệu lực", "B. Thời điểm thông qua", "C. Thời điểm ký ban hành", "D. Thời điểm đăng công báo"], 0,
     "Văn bản quy phạm pháp luật được áp dụng từ thời điểm bắt đầu có hiệu lực."),

    ("4. Quy phạm PL, Hệ thống PL & Văn bản QPPL", "PLDC1 - Câu 24",
     "Bộ phận \"giả định\" có ý nghĩa như thế nào trong quy phạm pháp luật?",
     ["A. Xác định chủ thể, điều kiện, hoàn cảnh, tình huống chịu sự tác động của QPPL", "B. Xác định cách xử sự của các chủ thể pháp luật khi tham gia vào quan hệ xã hội", "C. Xác định biện pháp xử lý đối với chủ thể vi phạm pháp luật", "D. Tùy từng trường hợp mà có một trong các ý nghĩa nêu trên"], 0,
     "Giả định trả lời câu hỏi: Ai (chủ thể nào), trong điều kiện, hoàn cảnh nào thì chịu sự điều chỉnh của quy phạm."),

    ("4. Quy phạm PL, Hệ thống PL & Văn bản QPPL", "PLDC1 - Câu 25",
     "Quy phạm pháp luật bao gồm những loại nào?",
     ["A. Chỉ có một loại là quy phạm bắt buộc", "B. Chỉ có một loại là quy phạm cấm đoán", "C. Chỉ có một loại là quy phạm lựa chọn (cho phép)", "D. Có thể bao gồm tất cả các loại quy phạm nêu trên"], 3,
     "Quy phạm điều chỉnh có thể là quy phạm bắt buộc, quy phạm cấm đoán hoặc quy phạm trao quyền (lựa chọn)."),

    ("4. Quy phạm PL, Hệ thống PL & Văn bản QPPL", "PLDC1 - Câu 26 & PLDC9 - Câu 27",
     "Quy phạm \"Công dân được quyền tự do kinh doanh theo quy định của pháp luật\" (hoặc \"Mọi người có quyền tự do kinh doanh trong những ngành nghề mà pháp luật không cấm\") gồm những bộ phận nào?",
     ["A. Giả định, quy định, chế tài", "B. Giả định, quy định", "C. Giả định, chế tài", "D. Quy định, chế tài"], 1,
     "Chủ thể 'Công dân / Mọi người' là bộ phận Giả định; 'được quyền tự do kinh doanh...' là bộ phận Quy định (không có bộ phận Chế tài)."),

    ("4. Quy phạm PL, Hệ thống PL & Văn bản QPPL", "PLDC7 - Câu 2",
     "Các quy tắc xử sự nào sau đây là quy phạm pháp luật?",
     ["A. Những quy tắc xử sự bắt buộc trong tôn giáo", "B. Các chuẩn mực ứng xử chung giữa người với người được cộng đồng thừa nhận", "C. Những tập tục hình thành lâu đời được cộng đồng thừa nhận", "D. Những quy tắc xử sự được nhà nước ban hành hoặc thừa nhận và đảm bảo thực hiện"], 3,
     "Quy phạm pháp luật phải do Nhà nước ban hành hoặc thừa nhận và được Nhà nước đảm bảo thực hiện."),

    ("4. Quy phạm PL, Hệ thống PL & Văn bản QPPL", "PLDC7 - Câu 3",
     "Điền vào chỗ trống: \"Quy phạm pháp luật là quy tắc xử sự mang tính ... do ... ban hành và đảm bảo thực hiện, thể hiện ý chí và bảo vệ lợi ích của giai cấp thống trị để điều chỉnh các ...\"",
     ["A. bắt buộc chung / nhà nước / quan hệ pháp luật", "B. bắt buộc chung / nhà nước / quan hệ xã hội", "C. bắt buộc chung / quốc hội / quan hệ xã hội", "D. bắt buộc / nhà nước / quan hệ xã hội"], 1,
     "Quy phạm pháp luật mang tính bắt buộc chung, do Nhà nước ban hành để điều chỉnh các quan hệ xã hội."),

    ("4. Quy phạm PL, Hệ thống PL & Văn bản QPPL", "PLDC7 - Câu 4",
     "Quy phạm pháp luật là cách xử sự do nhà nước quy định để:",
     ["A. Áp dụng trong một hoàn cảnh cụ thể", "B. Áp dụng trong nhiều hoàn cảnh", "C. Cả A và B đều đúng (theo đáp án bộ đề PLDC7)", "D. Cả A và B đều sai"], 2,
     "Theo đáp án gốc của bộ đề PLDC7 (Câu 4) là Cả A và B đều đúng."),

    ("4. Quy phạm PL, Hệ thống PL & Văn bản QPPL", "PLDC7 - Câu 5",
     "Quy phạm pháp luật bắt nguồn từ đâu?",
     ["A. Từ ý thức chủ quan của các cá nhân trong xã hội", "B. Từ tư duy trừu tượng của con người", "C. Từ thực tiễn đời sống xã hội", "D. Từ thần linh"], 2,
     "Quy phạm pháp luật bắt nguồn từ nhu cầu và thực tiễn đời sống xã hội."),

    ("4. Quy phạm PL, Hệ thống PL & Văn bản QPPL", "PLDC7 - Câu 6",
     "Quy phạm pháp luật là cách xử sự do nhà nước quy định để:",
     ["A. Áp dụng cho một lần duy nhất và vẫn còn hiệu lực", "B. Áp dụng cho nhiều lần và hết hiệu lực ngay sau đó", "C. Áp dụng cho một lần duy nhất và hết hiệu lực sau lần áp dụng đó", "D. Áp dụng cho nhiều lần và vẫn còn hiệu lực sau những lần áp dụng đó"], 3,
     "Quy phạm pháp luật được áp dụng lặp đi lặp lại nhiều lần và vẫn còn hiệu lực cho đến khi bị sửa đổi, bãi bỏ hoặc thay thế."),

    ("4. Quy phạm PL, Hệ thống PL & Văn bản QPPL", "PLDC7 - Câu 9",
     "Bộ phận giả định của quy phạm pháp luật:",
     ["A. Nêu rõ hoàn cảnh, điều kiện mà cá nhân, tổ chức không phải xử sự theo quy định của Nhà nước", "B. Nêu rõ hoàn cảnh, điều kiện cụ thể của cuộc sống mà khi hoàn cảnh, điều kiện đó xuất hiện, cá nhân, tổ chức ở vào điều kiện, hoàn cảnh này phải xử sự theo quy định của Nhà nước", "C. Nêu rõ hoàn cảnh, điều kiện không cụ thể của cuộc sống", "D. Nêu rõ cách (quy tắc) xử sự mà mọi chủ thể phải xử sự theo"], 1,
     "Bộ phận giả định nêu rõ chủ thể, điều kiện, hoàn cảnh cụ thể chịu sự điều chỉnh của quy phạm pháp luật."),

    ("4. Quy phạm PL, Hệ thống PL & Văn bản QPPL", "PLDC7 - Câu 10",
     "Bộ phận quy định của quy phạm pháp luật:",
     ["A. Nêu biện pháp xử lý dự kiến áp dụng đối với người vi phạm", "B. Nêu rõ hoàn cảnh, điều kiện không cụ thể của cuộc sống", "C. Nêu rõ cách (quy tắc) xử sự mà mọi chủ thể (cá nhân, tổ chức) phải xử sự theo khi họ ở vào hoàn cảnh, điều kiện đã nêu trong phần giả định", "D. Nêu rõ chủ thể chịu sự tác động của pháp luật"], 2,
     "Bộ phận quy định nêu rõ quy tắc xử sự (được làm gì, không được làm gì, phải làm gì) khi ở vào hoàn cảnh đã nêu ở giả định."),

    ("4. Quy phạm PL, Hệ thống PL & Văn bản QPPL", "PLDC7 - Câu 11",
     "Bộ phận chế tài có ý nghĩa:",
     ["A. Nêu rõ hoàn cảnh, điều kiện cụ thể của cuộc sống", "B. Nêu rõ hoàn cảnh, điều kiện không cụ thể", "C. Nêu rõ cách (quy tắc) xử sự mà mọi chủ thể phải tuân theo", "D. Nêu biện pháp xử lý dự kiến sẽ được áp dụng đối với người xử sự không đúng hoặc làm trái quy định của nhà nước - trái với nội dung được ghi trong phần quy định"], 3,
     "Chế tài nêu hậu quả pháp lý bất lợi (biện pháp xử lý dự kiến) đối với chủ thể vi phạm."),

    ("4. Quy phạm PL, Hệ thống PL & Văn bản QPPL", "PLDC7 - Câu 12",
     "Có mấy loại chế tài cơ bản?",
     ["A. 2 loại: chế tài dân sự, chế tài kỷ luật", "B. 3 loại: chế tài hình sự, chế tài hành chính, chế tài dân sự", "C. 2 loại: chế tài hình sự, chế tài hành chính", "D. 4 loại: chế tài hình sự, chế tài hành chính, chế tài dân sự, chế tài kỷ luật"], 3,
     "Có 4 loại chế tài tương ứng với 4 loại trách nhiệm pháp lý: hình sự, hành chính, dân sự, kỷ luật."),

    ("4. Quy phạm PL, Hệ thống PL & Văn bản QPPL", "PLDC7 - Câu 13",
     "Chế tài của quy phạm pháp luật là:",
     ["A. Hình phạt nghiêm khắc của nhà nước đối với người có hành vi vi phạm pháp luật", "B. Những hậu quả bất lợi có thể áp dụng đối với người không thực hiện hoặc thực hiện không đúng quy định của quy phạm pháp luật", "C. Biện pháp cưỡng chế mà nhà nước áp dụng đối với người vi phạm pháp luật", "D. Cả A, B và C đều đúng (theo đáp án bộ đề PLDC7)"], 3,
     "Theo đáp án gốc của bộ đề PLDC7 (Câu 13) là Cả A, B và C đều đúng."),

    ("4. Quy phạm PL, Hệ thống PL & Văn bản QPPL", "PLDC7 - Câu 14",
     "Phần tử nhỏ nhất của hệ thống pháp luật Việt Nam là:",
     ["A. Điều luật", "B. Quy phạm pháp luật", "C. Cả điều luật và quy phạm pháp luật", "D. Chế định pháp luật"], 1,
     "Quy phạm pháp luật là tế bào (phần tử nhỏ nhất) cấu thành nên hệ thống pháp luật."),

    ("4. Quy phạm PL, Hệ thống PL & Văn bản QPPL", "PLDC7 - Câu 15",
     "\"Việc kết hôn phải được đăng ký tại cơ quan nhà nước có thẩm quyền, mọi hình thức kết hôn khác đều không có giá trị về mặt pháp lý.\" Quy phạm pháp luật này gồm có mấy bộ phận?",
     ["A. 4", "B. 1", "C. 3", "D. 2"], 3,
     "Theo đáp án gốc của bộ đề PLDC7 (Câu 15) là 2 bộ phận."),

    ("4. Quy phạm PL, Hệ thống PL & Văn bản QPPL", "PLDC8 - Câu 12",
     "Văn bản có giá trị pháp lý cao nhất trong hệ thống các văn bản pháp luật Việt Nam là:",
     ["A. Hiến pháp", "B. Bộ luật của Quốc hội", "C. Nghị quyết của Quốc hội", "D. Thông tư của Bộ trưởng"], 0,
     "Hiến pháp là đạo luật cơ bản, có hiệu lực pháp lý tối cao trong hệ thống văn bản quy phạm pháp luật."),

    ("4. Quy phạm PL, Hệ thống PL & Văn bản QPPL", "PLDC8 - Câu 13",
     "Sắp xếp theo thứ tự nhỏ dần của hình thức bên trong của pháp luật:",
     ["A. Quy phạm pháp luật, hệ thống pháp luật, ngành luật, chế định luật", "B. Ngành luật, quy phạm pháp luật, hệ thống pháp luật, chế định luật", "C. Hệ thống pháp luật, ngành luật, chế định luật, quy phạm pháp luật", "D. Chế định pháp luật, quy phạm pháp luật, hệ thống pháp luật, ngành luật"], 2,
     "Từ lớn đến nhỏ: Hệ thống pháp luật -> Ngành luật -> Chế định pháp luật -> Quy phạm pháp luật."),

    ("4. Quy phạm PL, Hệ thống PL & Văn bản QPPL", "PLDC8 - Câu 23",
     "Văn bản quy phạm pháp luật là:",
     ["A. Văn bản do cơ quan nhà nước có thẩm quyền ban hành", "B. Chứa đựng các quy tắc xử sự mang tính bắt buộc chung được nhà nước đảm bảo thực hiện", "C. Được áp dụng nhiều lần trong thực tế cuộc sống", "D. Cả ba phương án A, B và C"], 3,
     "Văn bản QPPL hội tụ đủ cả 3 đặc điểm trên."),

    ("4. Quy phạm PL, Hệ thống PL & Văn bản QPPL", "PLDC8 - Câu 25",
     "Chế định pháp luật là gì?",
     ["A. Là một nhóm các quy phạm pháp luật bất kỳ", "B. Là văn bản do cơ quan nhà nước có thẩm quyền ban hành", "C. Là toàn bộ các quy phạm pháp luật trong xã hội", "D. Là một nhóm các Quy phạm pháp luật điều chỉnh một nhóm quan hệ xã hội cùng loại, có tính chất nội tại trong một ngành luật"], 3,
     "Chế định pháp luật là tập hợp một nhóm các quy phạm pháp luật điều chỉnh một nhóm quan hệ xã hội cùng loại có liên hệ mật thiết với nhau trong một ngành luật."),

    ("4. Quy phạm PL, Hệ thống PL & Văn bản QPPL", "PLDC8 - Câu 30",
     "Bộ phận giả định trong quy phạm pháp luật sau là: “Người nào quảng cáo gian dối về hàng hóa, dịch vụ gây hậu quả nghiêm trọng đã bị xử phạt hành chính về hành vi này hoặc đã bị kết án về tội này, chưa được xóa án tích mà còn vi phạm thì bị phạt tiền từ 10 triệu đến 100 triệu đồng, cải tạo không giam giữ đến 3 năm hoặc bị phạt tù từ 6 tháng đến 3 năm.”",
     ["A. Người nào quảng cáo gian dối về hàng hóa, dịch vụ", "B. Người nào quảng cáo gian dối về hàng hóa dịch vụ gây hậu quả nghiêm trọng", "C. Người nào quảng cáo gian dối về hàng hóa dịch vụ gây hậu quả nghiêm trọng đã bị xử phạt hành chính vì hành vi này", "D. Người nào quảng cáo gian dối về hàng hóa, dịch vụ gây hậu quả nghiêm trọng đã bị xử phạt hành chính về hành vi này hoặc đã bị kết án vì tội này, chưa được xóa án tích mà còn vi phạm"], 3,
     "Toàn bộ phần mô tả chủ thể và điều kiện hoàn cảnh trước từ 'thì bị phạt tiền...' là bộ phận Giả định (phần sau là Chế tài)."),

    ("4. Quy phạm PL, Hệ thống PL & Văn bản QPPL", "PLDC9 - Câu 29",
     "Hệ thống pháp luật gồm:",
     ["A. Hệ thống cấu trúc của pháp luật và hệ thống văn bản pháp luật (hệ thống nguồn)", "B. Quy phạm pháp luật, chế định pháp luật, ngành luật", "C. Tập hợp hóa và pháp điển hóa", "D. Tất cả các phương án trên đều sai"], 0,
     "Hệ thống pháp luật gồm 2 mặt: Hệ thống cấu trúc bên trong (QPPL, chế định, ngành luật) và Hệ thống văn bản pháp luật (hình thức bên ngoài)."),

    # =========================================================================
    # PHẦN 5: QUAN HỆ PHÁP LUẬT, CHỦ THỂ & SỰ KIỆN PHÁP LÝ
    # =========================================================================
    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC1 - Câu 27 & PLDC3 - Câu 16",
     "Chủ thể của quan hệ pháp luật là:",
     ["A. Bất kỳ cá nhân nào", "B. Tất cả các cá nhân, tổ chức tham gia vào quan hệ xã hội", "C. Mọi tổ chức", "D. Các cá nhân, pháp nhân (tổ chức) có đầy đủ năng lực chủ thể theo quy định của pháp luật"], 3,
     "Cá nhân, tổ chức muốn trở thành chủ thể của quan hệ pháp luật phải có năng lực chủ thể (gồm năng lực pháp luật và năng lực hành vi)."),

    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC1 - Câu 28 & PLDC3 - Câu 17",
     "Nhận định nào dưới đây là SAI?",
     ["A. Năng lực pháp luật của mọi tổ chức là như nhau", "B. Năng lực pháp luật của tổ chức xuất hiện khi tổ chức đó được thành lập", "C. Năng lực pháp luật của mọi cá nhân là như nhau", "D. Năng lực pháp luật của cá nhân xuất hiện khi cá nhân đó sinh ra và mất đi khi cá nhân đó chết"], 0,
     "Năng lực pháp luật của mỗi tổ chức là KHÁC NHAU, phụ thuộc vào mục đích, chức năng, lĩnh vực hoạt động đăng ký của từng tổ chức."),

    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC1 - Câu 35 & PLDC7 - Câu 20",
     "Tư cách pháp nhân dùng để chỉ:",
     ["A. Tư cách chủ thể pháp luật của cá nhân", "B. Tư cách chủ thể pháp luật của cá nhân và tổ chức", "C. Tư cách chủ thể pháp luật của tổ chức (đáp ứng đủ điều kiện luật định)", "D. Cả A, B, C đều sai"], 2,
     "Pháp nhân là khái niệm chỉ tư cách chủ thể pháp luật của tổ chức có đủ điều kiện theo quy định của pháp luật."),

    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC3 - Câu 13",
     "Quan hệ xã hội muốn trở thành quan hệ pháp luật cần có điều kiện gì?",
     ["A. Có sự kiện pháp lý", "B. Có quy phạm pháp luật điều chỉnh", "C. Có chủ thể tham gia quan hệ pháp luật và chủ thể đó có đủ năng lực chủ thể", "D. Phải có đủ ba điều kiện trên"], 3,
     "Quan hệ pháp luật hình thành khi có đủ 3 điều kiện: Quy phạm pháp luật, Chủ thể có năng lực chủ thể và Sự kiện pháp lý."),

    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC3 - Câu 14",
     "Các yếu tố cấu thành của quan hệ pháp luật gồm:",
     ["A. Chủ thể, khách thể của quan hệ pháp luật", "B. Nội dung của quan hệ pháp luật", "C. Sự kiện pháp lý", "D. Cả A và B (Chủ thể, Khách thể và Nội dung của quan hệ pháp luật)"], 3,
     "Cấu trúc của một quan hệ pháp luật gồm 3 yếu tố: Chủ thể, Khách thể và Nội dung."),

    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC3 - Câu 15",
     "Nhận định nào sau đây là đúng về quan hệ pháp luật?",
     ["A. Quan hệ pháp luật luôn phản ánh ý chí của nhà nước", "B. Quan hệ pháp luật phản ánh ý chí của các bên tham gia quan hệ trong khuôn khổ pháp luật", "C. Quan hệ pháp luật được đảm bảo bằng sức mạnh cưỡng chế của nhà nước", "D. Tất cả các nhận định trên đều đúng"], 3,
     "Quan hệ pháp luật mang tính ý chí (ý chí nhà nước và ý chí các bên) và được đảm bảo thực hiện bằng cưỡng chế nhà nước."),

    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC3 - Câu 18",
     "Năng lực chủ thể gồm những loại năng lực nào?",
     ["A. Năng lực pháp luật và năng lực hành vi", "B. Chỉ có năng lực pháp luật", "C. Chỉ có năng lực hành vi", "D. Năng lực pháp luật và năng lực hành chính"], 0,
     "Năng lực chủ thể gồm 2 yếu tố: Năng lực pháp luật và Năng lực hành vi."),

    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC3 - Câu 19",
     "Năng lực chủ thể được hiểu là:",
     ["A. Khả năng chủ thể có các quyền và nghĩa vụ pháp lý do nhà nước thừa nhận", "B. Khả năng chủ thể có thể trở thành các bên tham gia vào các quan hệ pháp luật", "C. Khả năng chủ thể bằng hành vi của mình thực hiện trên thực tế các quyền và nghĩa vụ pháp lý", "D. Tất cả đều sai"], 1,
     "Theo đáp án gốc của bộ đề PLDC3 (Câu 19), năng lực chủ thể là khả năng chủ thể có thể trở thành các bên tham gia vào các quan hệ pháp luật."),

    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC3 - Câu 20",
     "Năng lực pháp luật là gì?",
     ["A. Khả năng chủ thể có thể trở thành các bên tham gia vào các quan hệ pháp luật", "B. Khả năng chủ thể có các quyền và nghĩa vụ pháp lý do nhà nước thừa nhận", "C. Khả năng chủ thể bằng hành vi của mình thực hiện trên thực tế các quyền và nghĩa vụ pháp lý", "D. Tất cả đều đúng"], 1,
     "Năng lực pháp luật là khả năng có quyền và nghĩa vụ pháp lý do Nhà nước quy định/thừa nhận cho các chủ thể."),

    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC3 - Câu 21",
     "Năng lực hành vi được hiểu là:",
     ["A. Khả năng chủ thể bằng hành vi của mình thực hiện trên thực tế các quyền và nghĩa vụ pháp lý", "B. Tất cả đều đúng", "C. Khả năng chủ thể có các quyền và nghĩa vụ pháp lý do nhà nước thừa nhận", "D. Khả năng chủ thể có tài sản riêng"], 0,
     "Năng lực hành vi là khả năng mà chủ thể bằng chính hành vi của mình xác lập và thực hiện các quyền, nghĩa vụ pháp lý."),

    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC3 - Câu 22",
     "Nhận định nào dưới đây là đúng?",
     ["A. Năng lực pháp luật luôn mang tính giai cấp", "B. Năng lực hành vi luôn mang tính giai cấp", "C. Năng lực pháp luật của mọi tổ chức là như nhau", "D. Năng lực pháp luật là điều kiện đủ, năng lực hành vi là điều kiện cần"], 0,
     "Năng lực pháp luật do Nhà nước quy định nên luôn phản ánh ý chí nhà nước và mang tính giai cấp (Năng lực pháp luật là điều kiện cần, năng lực hành vi là điều kiện đủ)."),

    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC3 - Câu 23",
     "Chủ thể của quan hệ pháp luật là cá nhân bao gồm những loại nào?",
     ["A. Tất cả các phương án trên (Công dân Việt Nam, Người nước ngoài, Người không có quốc tịch)", "B. Chỉ có công dân Việt Nam", "C. Chỉ có người không có quốc tịch sinh sống trên lãnh thổ Việt Nam", "D. Chỉ có người nước ngoài sinh sống trên lãnh thổ Việt Nam"], 0,
     "Cá nhân là chủ thể QHPL gồm: Công dân nước sở tại, người nước ngoài và người không quốc tịch."),

    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC3 - Câu 24",
     "Năng lực hành vi của cá nhân phụ thuộc vào:",
     ["A. Độ tuổi và hoàn cảnh kinh tế", "B. Khả năng nhận thức", "C. Độ tuổi", "D. Độ tuổi và khả năng nhận thức (khả năng điều khiển hành vi)"], 3,
     "Năng lực hành vi của cá nhân phụ thuộc vào độ tuổi và khả năng nhận thức, làm chủ hành vi."),

    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC5 - Câu 1",
     "Năng lực pháp luật của cá nhân phụ thuộc vào:",
     ["A. Hoàn cảnh kinh tế của cá nhân đó", "B. Độ tuổi và khả năng nhận thức của cá nhân đó", "C. Pháp luật của từng quốc gia", "D. B và C đúng"], 2,
     "Năng lực pháp luật là thuộc tính chính trị - pháp lý do Nhà nước quy định, nên phụ thuộc vào pháp luật của từng quốc gia."),

    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC5 - Câu 2",
     "Anh A mới ký hợp đồng với công ty X để mua một chiếc xe ô tô với trị giá 1 tỷ. Xác định khách thể của quan hệ pháp luật nói trên (theo đáp án bộ đề PLDC5):",
     ["A. Quyền sở hữu chiếc xe ô tô", "B. Quyền sử dụng chiếc xe ô tô", "C. Chiếc xe ô tô", "D. Số tiền 1 tỷ"], 0,
     "Khách thể của quan hệ pháp luật là lợi ích mà các bên hướng tới (quyền sở hữu đối với chiếc xe ô tô và khoản tiền thanh toán)."),

    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC5 - Câu 3",
     "Nhận định nào sau đây là SAI về năng lực pháp luật của cá nhân?",
     ["A. Năng lực pháp luật của cá nhân là khác nhau", "B. Năng lực pháp luật của cá nhân xuất hiện khi cá nhân đó sinh ra", "C. Năng lực pháp luật của cá nhân mất đi khi cá nhân đó chết", "D. Đáp án B, C đúng"], 0,
     "Mọi cá nhân đều bình đẳng trước pháp luật nên năng lực pháp luật của mọi cá nhân là như nhau. Nhận định 'khác nhau' là sai."),

    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC5 - Câu 4",
     "Nhận định nào sau đây là SAI về năng lực chủ thể của tổ chức?",
     ["A. Tất cả các nhận định B, C, D đều đúng (không có nhận định nào sai)", "B. Năng lực pháp luật của tổ chức xuất hiện khi tổ chức đó được thành lập", "C. Năng lực pháp luật, năng lực hành vi của tổ chức xuất hiện đồng thời cùng một lúc kể từ thời điểm tổ chức đó được thành lập", "D. Năng lực pháp luật của tổ chức mất đi khi tổ chức đó bị giải thể"], 0,
     "Cả 3 nhận định B, C, D đều đúng nên đáp án ở câu hỏi 'Nhận định nào sai' là A (Tất cả đều không sai)."),

    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC5 - Câu 5",
     "Nội dung của quan hệ pháp luật bao gồm:",
     ["A. Gồm các quyền chủ thể của các bên tham gia quan hệ pháp luật", "B. Đồng nghĩa với năng lực pháp luật", "C. Gồm các nghĩa vụ pháp lý của các bên tham gia quan hệ pháp luật", "D. Cả A và C đúng (Gồm quyền chủ thể và nghĩa vụ pháp lý của các bên)"], 3,
     "Nội dung của quan hệ pháp luật bao gồm quyền chủ thể và nghĩa vụ pháp lý của các bên tham gia."),

    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC5 - Câu 6",
     "Quyền của chủ thể là cách xử sự mà pháp luật:",
     ["A. Cho phép chủ thể thực hiện", "B. Khuyến khích chủ thể thực hiện", "C. Cả A và B đúng", "D. Cấm chủ thể thực hiện"], 2,
     "Theo đáp án gốc của bộ đề PLDC5 (Câu 6), quyền chủ thể là cách xử sự mà pháp luật cho phép và khuyến khích chủ thể thực hiện."),

    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC5 - Câu 7",
     "Quyền của chủ thể được biểu hiện ở các khía cạnh nào sau đây?",
     ["A. Quyền thụ hưởng", "B. Quyền sử dụng, quyền sở hữu", "C. Quyền chuyển nhượng", "D. Cả 3 đáp án trên"], 3,
     "Quyền chủ thể biểu hiện đa dạng qua quyền thụ hưởng, sở hữu, sử dụng, chuyển nhượng..."),

    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC5 - Câu 8",
     "Nhận định nào sau đây là đúng về việc thực hiện quyền chủ thể?",
     ["A. Chủ thể bắt buộc phải thực hiện quyền của mình", "B. Nhà nước luôn ép buộc chủ thể phải thực hiện quyền của mình", "C. Cả A, B, D đều sai", "D. Chủ thể có thể không thực hiện quyền của mình"], 3,
     "Đối với quyền chủ thể (quy phạm trao quyền), chủ thể có quyền tự do lựa chọn thực hiện hoặc không thực hiện."),

    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC5 - Câu 9",
     "Nghĩa vụ pháp lý là cách xử sự mà pháp luật:",
     ["A. Bắt buộc chủ thể phải thực hiện để đáp ứng quyền của chủ thể bên kia", "B. Cấm chủ thể thực hiện", "C. Khuyến khích chủ thể thực hiện", "D. Cho phép chủ thể tự do lựa chọn"], 0,
     "Nghĩa vụ pháp lý là cách xử sự bắt buộc phải thực hiện nhằm đáp ứng quyền của chủ thể phía bên kia."),

    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC5 - Câu 10",
     "Đặc điểm của nghĩa vụ pháp lý là:",
     ["A. Có tính chất pháp lý", "B. Bắt buộc phải thực hiện, có thể được áp dụng cho các mối quan hệ pháp lý khác nhau", "C. Được áp đặt bởi pháp luật", "D. Cả 3 đáp án trên"], 3,
     "Theo đáp án gốc của bộ đề PLDC5 (Câu 10) là Cả 3 đáp án trên."),

    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC5 - Câu 11",
     "Khách thể của quan hệ pháp luật là:",
     ["A. Lợi ích mà các bên mong muốn đạt được khi tham gia quan hệ pháp luật", "B. Yếu tố thúc đẩy các bên tham gia quan hệ pháp luật", "C. Cả A và B đúng", "D. Quyền và nghĩa vụ của các bên"], 2,
     "Khách thể của QHPL là những lợi ích (vật chất, tinh thần, chính trị...) mà các bên mong muốn đạt được, thúc đẩy chủ thể tham gia QHPL."),

    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC5 - Câu 12",
     "Sự kiện pháp lý là gì?",
     ["A. Là những hoàn cảnh, tình huống trong thực tế", "B. Làm phát sinh, thay đổi và chấm dứt các quan hệ pháp luật", "C. Cả A và B đúng", "D. Là yếu tố thúc đẩy các bên tham gia quan hệ pháp luật"], 2,
     "Sự kiện pháp lý là những hoàn cảnh, tình huống thực tế mà pháp luật gắn sự xuất hiện của chúng với sự phát sinh, thay đổi hoặc chấm dứt QHPL."),

    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC5 - Câu 13",
     "Sự kiện pháp lý gồm mấy loại (theo tiêu chí ý chí)?",
     ["A. Các hành vi pháp lý và sự biến pháp lý", "B. Các hành vi thực tế", "C. Các sự biến pháp lý", "D. Các hành vi và sự kiện thông thường"], 0,
     "Theo tiêu chí ý chí, sự kiện pháp lý được chia thành 2 loại: Hành vi pháp lý và Sự biến pháp lý."),

    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC5 - Câu 14",
     "Tác động của sự kiện pháp lý đối với quan hệ pháp luật là:",
     ["A. Tất cả các phương án (Làm phát sinh, thay đổi, chấm dứt quan hệ pháp luật)", "B. Chỉ làm phát sinh quan hệ pháp luật", "C. Chỉ làm chấm dứt quan hệ pháp luật", "D. Chỉ làm thay đổi quan hệ pháp luật"], 0,
     "Sự kiện pháp lý có thể làm phát sinh, thay đổi hoặc chấm dứt quan hệ pháp luật."),

    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC5 - Câu 15",
     "Nhận định nào sau đây là đúng về sự biến pháp lý?",
     ["A. Sự biến là sự kiện pháp lý phổ biến nhất do con người tạo ra", "B. Sự biến là sự kiện pháp lý phụ thuộc vào ý chí của con người", "C. Sự biến là sự kiện pháp lý được thực hiện dưới dạng hành động có mục đích", "D. Sự biến là sự kiện pháp lý không phụ thuộc vào ý chí của con người"], 3,
     "Sự biến pháp lý là những hiện tượng tự nhiên, khách quan xảy ra không phụ thuộc vào ý chí của con người (như bão, lũ lụt, cái chết tự nhiên...)."),

    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC5 - Câu 16",
     "Hành vi pháp lý là loại sự kiện pháp lý:",
     ["A. Không phụ thuộc vào ý chí của con người", "B. Phụ thuộc vào ý chí của con người", "C. Phổ biến trong thực tiễn cuộc sống", "D. Cả B và C đúng"], 3,
     "Hành vi pháp lý là những sự kiện xảy ra theo ý chí của con người và là loại sự kiện pháp lý phổ biến nhất trong thực tiễn."),

    ("5. Quan hệ pháp luật, Chủ thể & Sự kiện pháp lý", "PLDC7 - Câu 21",
     "Hành vi của pháp nhân được thực hiện bởi ai?",
     ["A. Người điều hành hoạt động của pháp nhân", "B. Người đại diện theo pháp luật của pháp nhân", "C. Người quản lý pháp nhân", "D. Người lao động trong pháp nhân"], 1,
     "Pháp nhân tham gia vào các quan hệ pháp luật thông qua hành vi của người đại diện hợp pháp (người đại diện theo pháp luật / theo ủy quyền)."),

    # =========================================================================
    # PHẦN 6: THỰC HIỆN PHÁP LUẬT, VI PHẠM PHÁP LUẬT & TRÁCH NHIỆM PHÁP LÝ
    # =========================================================================
    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC1 - Câu 29 & PLDC4 - Câu 12",
     "Đội mũ bảo hiểm khi tham gia giao thông bằng xe gắn máy chính là chủ thể đang thực hiện pháp luật dưới hình thức nào?",
     ["A. Tuân thủ pháp luật", "B. Thi hành (chấp hành) pháp luật", "C. Sử dụng pháp luật", "D. Áp dụng pháp luật"], 1,
     "Đội mũ bảo hiểm là chủ động thực hiện nghĩa vụ bắt buộc bằng hành vi tích cực -> Thi hành (chấp hành) pháp luật."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC1 - Câu 30 & PLDC4 - Câu 24",
     "Hành vi trái pháp luật thực hiện trong trường hợp nào sau đây thì KHÔNG bị coi là có lỗi (không phải chịu trách nhiệm pháp lý)?",
     ["A. Sự kiện bất ngờ", "B. Tình thế cấp thiết", "C. Phòng vệ chính đáng", "D. Tất cả các trường hợp trên"], 3,
     "Trong sự kiện bất ngờ, tình thế cấp thiết và phòng vệ chính đáng, chủ thể không bị coi là có lỗi."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC1 - Câu 31 & PLDC4 - Câu 28",
     "Chủ thể không thấy trước hành vi của mình có thể gây ra hậu quả nguy hại cho xã hội, mặc dù phải thấy trước và có thể thấy trước hậu quả đó thì:",
     ["A. Chủ thể có lỗi vô ý do cẩu thả", "B. Chủ thể có lỗi cố ý gián tiếp", "C. Chủ thể có lỗi vô ý do quá tự tin", "D. Chủ thể không có lỗi vì không nhận thức được hậu quả"], 0,
     "Không thấy trước hậu quả mặc dù buộc phải thấy trước và có thể thấy trước là dấu hiệu của lỗi vô ý do cẩu thả."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC1 - Câu 32",
     "Khái niệm \"trách nhiệm pháp lý\" được hiểu như thế nào?",
     ["A. Là quan hệ pháp luật đặc biệt phát sinh giữa Nhà nước và chủ thể vi phạm pháp luật trong việc nhà nước áp dụng chế tài đối với chủ thể vi phạm pháp luật", "B. Là quan hệ pháp luật đặc biệt phát sinh giữa các chủ thể vi phạm pháp luật với nhau", "C. Là quan hệ phát sinh giữa các cơ quan nhà nước với nhau", "D. Là nghĩa vụ đạo đức của mọi công dân"], 0,
     "Trách nhiệm pháp lý là quan hệ pháp luật đặc biệt giữa Nhà nước (thông qua cơ quan có thẩm quyền) và chủ thể vi phạm pháp luật."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC1 - Câu 33 & PLDC4 - Câu 37",
     "Quyết định xử phạt đối với người điều khiển xe máy vượt đèn đỏ là loại trách nhiệm pháp lý gì?",
     ["A. Trách nhiệm hành chính", "B. Trách nhiệm dân sự", "C. Trách nhiệm hình sự", "D. Trách nhiệm kỷ luật"], 0,
     "Vượt đèn đỏ là vi phạm hành chính nên chịu trách nhiệm hành chính."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC3 - Câu 28",
     "Cơ sở nào làm phát sinh trách nhiệm pháp lý?",
     ["A. Khi có quy phạm pháp luật được ban hành", "B. Khi cơ quan có thẩm quyền tiến hành xem xét vụ việc", "C. Khi có chủ thể pháp luật xuất hiện", "D. Khi có hành vi vi phạm pháp luật và có quyết định áp dụng pháp luật của cơ quan có thẩm quyền"], 3,
     "Cơ sở thực tiễn là hành vi vi phạm pháp luật và cơ sở pháp lý là quyết định áp dụng pháp luật có hiệu lực của cơ quan có thẩm quyền."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC4 - Câu 7",
     "Có mấy hình thức thực hiện pháp luật?",
     ["A. 3", "B. 4", "C. 2", "D. 5"], 1,
     "Có 4 hình thức thực hiện pháp luật: Tuân thủ pháp luật, Thi hành (chấp hành) pháp luật, Sử dụng (vận dụng) pháp luật và Áp dụng pháp luật."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC4 - Câu 8",
     "Chủ thể thực hiện áp dụng pháp luật là ai?",
     ["A. Mọi cơ quan công chức nhà nước", "B. Mọi cá nhân, tổ chức", "C. Các cơ quan, công chức nhà nước có thẩm quyền (hoặc tổ chức được trao quyền)", "D. Ai cũng có quyền áp dụng pháp luật"], 2,
     "Chỉ các cơ quan, công chức nhà nước có thẩm quyền mới được thực hiện hình thức Áp dụng pháp luật."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC4 - Câu 9",
     "Tuân thủ pháp luật là gì?",
     ["A. Hình thức thực hiện những quy định về quyền chủ thể của pháp luật", "B. Hình thức thực hiện những quy định trao nghĩa vụ bắt buộc bằng hành động tích cực", "C. Hình thức thực hiện những QPPL mang tính chất ngăn cấm bằng hành vi thụ động, trong đó các chủ thể pháp luật kiềm chế không làm những việc mà pháp luật cấm", "D. Cả A và B"], 2,
     "Tuân thủ pháp luật là kiềm chế không làm những điều mà pháp luật cấm."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC4 - Câu 10",
     "Chấp hành (thi hành) pháp luật là gì?",
     ["A. Không làm những việc mà pháp luật cấm", "B. Thực hiện các quyền mà pháp luật quy định", "C. Phải thực hiện đúng các nghĩa vụ mà pháp luật quy định bằng hành vi tích cực", "D. Cả ba hoạt động trên"], 2,
     "Chấp hành (thi hành) pháp luật là chủ động thực hiện các nghĩa vụ pháp lý do pháp luật bắt buộc."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC4 - Câu 11",
     "Vận dụng (sử dụng) pháp luật là gì?",
     ["A. Thực hiện các QPPL bắt buộc", "B. Thực hiện các QPPL cấm đoán", "C. Thực hiện các QPPL cho phép (thực hiện quyền của mình)", "D. Cả ba đều đúng"], 2,
     "Sử dụng (vận dụng) pháp luật là việc chủ thể thực hiện các quyền mà pháp luật cho phép."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC4 - Câu 13",
     "Vi phạm pháp luật là khi chủ thể có năng lực trách nhiệm pháp lý:",
     ["A. Thực hiện hành vi cụ thể trái với quy định của pháp luật, có lỗi của chủ thể", "B. Chỉ có suy nghĩ trái pháp luật", "C. Thực hiện hành vi hợp pháp", "D. Không có đáp án nào đúng"], 0,
     "Vi phạm pháp luật phải là hành vi xác định, trái pháp luật, có lỗi và do chủ thể có năng lực trách nhiệm pháp lý thực hiện."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC4 - Câu 14",
     "Hành vi trái pháp luật được thể hiện dưới những dạng nào?",
     ["A. Thực hiện quyền vượt quá giới hạn pháp luật cho phép", "B. Thực hiện những gì mà pháp luật cấm", "C. Không thực hiện hoặc thực hiện không đúng những gì mà pháp luật yêu cầu", "D. Tất cả các trường hợp nêu trên"], 3,
     "Làm điều pháp luật cấm, không làm điều pháp luật bắt buộc, hoặc vượt quá giới hạn cho phép đều là hành vi trái pháp luật."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC4 - Câu 15",
     "Thực hiện pháp luật là gì?",
     ["A. Đó là hoạt động có mục đích của các chủ thể", "B. Đưa các quy định của pháp luật vào thực tế cuộc sống", "C. Tất cả các đáp án đều sai", "D. Đáp án A và B đều đúng"], 3,
     "Thực hiện pháp luật là hoạt động có mục đích nhằm hiện thực hóa các quy định pháp luật vào đời sống."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC4 - Câu 16",
     "Thực hiện 5K trong phòng chống dịch là chúng ta đang thực hiện pháp luật dưới hình thức nào?",
     ["A. Thi hành (chấp hành) pháp luật", "B. Tuân thủ pháp luật", "C. Áp dụng pháp luật", "D. Sử dụng pháp luật"], 0,
     "Thực hiện yêu cầu 5K là thực hiện nghĩa vụ bắt buộc bằng hành động tích cực -> Thi hành pháp luật."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC4 - Câu 17",
     "Hành vi trái pháp luật của chủ thể bị coi là có lỗi khi:",
     ["A. Chủ thể có khả năng nhận thức được hậu quả và có nhiều lựa chọn để thực hiện hành vi nhưng đã chọn cách thực hiện hành vi trái pháp luật", "B. Chủ thể thực hiện hành vi trong tình trạng mất năng lực hành vi", "C. Chủ thể gặp sự kiện bất ngờ", "D. Cả B và C"], 0,
     "Chủ thể bị coi là có lỗi khi có đủ điều kiện nhận thức và lựa chọn xử sự hợp pháp nhưng lại chọn xử sự trái pháp luật."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC4 - Câu 18",
     "Hành vi vi phạm pháp luật là những hành vi cụ thể của chủ thể được thể hiện dưới mấy dạng?",
     ["A. 3 dạng", "B. 4 dạng", "C. 1 dạng", "D. 2 dạng (Hành động và không hành động)"], 3,
     "Hành vi vi phạm pháp luật thể hiện dưới 2 dạng: Hành động (làm điều bị cấm) và Không hành động (không làm điều pháp luật bắt buộc)."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC4 - Câu 19",
     "Trong 4 trường hợp dưới đây, đâu là trường hợp cần có sự can thiệp của nhà nước (Áp dụng pháp luật) để pháp luật được thực hiện đúng?",
     ["A. Tất cả các đáp án đều đúng", "B. Khi áp dụng chế tài đối với những cá nhân, tổ chức vi phạm pháp luật", "C. Thực hiện 5K trong phòng chống dịch", "D. Đội mũ bảo hiểm khi đi ra đường"], 1,
     "Khi cần áp dụng biện pháp cưỡng chế / chế tài đối với người vi phạm thì bắt buộc phải có sự can thiệp của cơ quan nhà nước có thẩm quyền."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC4 - Câu 20",
     "Quyết định áp dụng pháp luật có giá trị:",
     ["A. Được đảm bảo thực hiện bằng sự cưỡng chế của nhà nước", "B. Có hiệu lực một lần", "C. Có hiệu lực đối với chủ thể cụ thể", "D. Tất cả các đáp án trên đều đúng"], 3,
     "Văn bản áp dụng pháp luật mang tính cá biệt, áp dụng một lần đối với cá nhân/tổ chức cụ thể và được đảm bảo bằng cưỡng chế nhà nước."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC4 - Câu 21",
     "Năng lực trách nhiệm pháp lý của chủ thể vi phạm pháp luật được xác định như thế nào?",
     ["A. Chỉ phụ thuộc vào hoàn cảnh gia đình", "B. Đối với tổ chức luôn có năng lực trách nhiệm pháp lý, cá nhân phụ thuộc vào độ tuổi và khả năng nhận thức", "C. Mọi cá nhân từ khi sinh ra đều có năng lực trách nhiệm pháp lý", "D. Chỉ có cá nhân mới có năng lực trách nhiệm pháp lý"], 1,
     "Tổ chức có năng lực trách nhiệm pháp lý từ khi thành lập; cá nhân chỉ có năng lực trách nhiệm pháp lý khi đạt độ tuổi luật định và có khả năng nhận thức."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC4 - Câu 22",
     "Mặt khách quan của vi phạm pháp luật gồm những dấu hiệu nào?",
     ["A. Mối quan hệ nhân quả giữa hành vi và hậu quả nguy hiểm cho xã hội", "B. Hậu quả nguy hiểm cho xã hội", "C. Hành vi trái pháp luật (cùng thời gian, địa điểm, công cụ vi phạm)", "D. Tất cả đáp án trên đều đúng"], 3,
     "Mặt khách quan gồm: Hành vi trái pháp luật, hậu quả nguy hiểm cho xã hội, mối quan hệ nhân quả, thời gian, địa điểm, phương tiện..."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC4 - Câu 23",
     "Các dấu hiệu cơ bản của vi phạm pháp luật là:",
     ["A. Có lỗi và do chủ thể có năng lực trách nhiệm pháp lý thực hiện", "B. Là hành vi cụ thể của chủ thể", "C. Là hành vi trái pháp luật xâm hại quan hệ xã hội được pháp luật bảo vệ", "D. Tất cả các dấu hiệu trên"], 3,
     "Vi phạm pháp luật phải hội tụ đủ 4 dấu hiệu: Hành vi xác định, tính trái pháp luật, có lỗi, và do chủ thể có năng lực trách nhiệm pháp lý thực hiện."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC4 - Câu 25",
     "Hậu quả do hành vi trái pháp luật gây ra cho xã hội là:",
     ["A. Chỉ là những thiệt hại về vật chất", "B. Những thiệt hại hoặc nguy cơ gây ra thiệt hại cho các quan hệ xã hội được pháp luật bảo vệ", "C. Chỉ là những thiệt hại về tinh thần", "D. Chỉ là những thiệt hại về thể chất"], 1,
     "Hậu quả của VPPL là những thiệt hại (vật chất, thể chất, tinh thần) hoặc nguy cơ gây thiệt hại cho các QHXH được pháp luật bảo vệ."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC4 - Câu 26",
     "Mặt chủ quan của vi phạm pháp luật bao gồm:",
     ["A. Động cơ", "B. Mục đích", "C. Lỗi", "D. Tất cả các đáp án trên"], 3,
     "Mặt chủ quan của vi phạm pháp luật gồm: Lỗi, động cơ và mục đích."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC4 - Câu 27",
     "Không mong muốn hậu quả xảy ra khi thực hiện hành vi trái pháp luật là đặc điểm của loại lỗi nào (theo đáp án bộ đề PLDC4)?",
     ["A. Lỗi cố ý gián tiếp", "B. Lỗi cố ý trực tiếp", "C. Không có đáp án nào đúng", "D. Lỗi vô ý nói chung"], 3,
     "Theo đáp án gốc của bộ đề PLDC4 (Câu 27) là D (Lỗi vô ý nói chung)."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC4 - Câu 29",
     "Trách nhiệm pháp lý được áp dụng đối với:",
     ["A. Mọi cá nhân trong xã hội", "B. Chủ thể thực hiện hành vi hợp pháp", "C. Chủ thể phòng vệ chính đáng", "D. Cá nhân, tổ chức vi phạm pháp luật"], 3,
     "Trách nhiệm pháp lý chỉ áp dụng đối với cá nhân, tổ chức có hành vi vi phạm pháp luật."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC4 - Câu 30",
     "Loại trách nhiệm pháp lý nào nghiêm khắc nhất?",
     ["A. Trách nhiệm dân sự", "B. Trách nhiệm hình sự", "C. Trách nhiệm hành chính", "D. Trách nhiệm kỷ luật"], 1,
     "Trách nhiệm hình sự là loại trách nhiệm pháp lý nghiêm khắc nhất (do Tòa án áp dụng đối với tội phạm)."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC4 - Câu 31 & Câu 36",
     "Trách nhiệm hành chính được áp dụng đối với người vi phạm hành chính thể hiện dưới dạng nào?",
     ["A. Hình phạt", "B. Buộc thôi việc", "C. Xử phạt hành chính", "D. Bồi thường thiệt hại"], 2,
     "Chế tài đặc trưng của trách nhiệm hành chính là xử phạt vi phạm hành chính."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC4 - Câu 32",
     "Trách nhiệm dân sự được thể hiện dưới những hình thức nào sau đây?",
     ["A. Tất cả các hình thức nêu trên (Bồi thường thiệt hại, phạt vi phạm, đính chính xin lỗi công khai)", "B. Chỉ bồi thường thiệt hại do vi phạm gây ra", "C. Chỉ phạt vi phạm", "D. Chỉ đính chính xin lỗi công khai"], 0,
     "Trách nhiệm dân sự gồm buộc xin lỗi, cải chính công khai, buộc thực hiện nghĩa vụ, phạt vi phạm, bồi thường thiệt hại..."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC4 - Câu 33",
     "Hình phạt là hình thức chế tài của loại trách nhiệm pháp lý nào?",
     ["A. Trách nhiệm hành chính", "B. Trách nhiệm dân sự", "C. Trách nhiệm hình sự", "D. Trách nhiệm kỷ luật"], 2,
     "Khái niệm 'Hình phạt' chỉ tồn tại trong Luật Hình sự (Trách nhiệm hình sự)."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC4 - Câu 34",
     "Một người đi xe máy lạng lách đánh võng ngoài đường dẫn đến va chạm giao thông và gây tai nạn thì lỗi gây tai nạn là lỗi gì?",
     ["A. Lỗi cố ý gián tiếp", "B. Lỗi cố ý trực tiếp", "C. Lỗi vô ý do cẩu thả", "D. Lỗi vô ý do quá tự tin"], 3,
     "Người lái xe thấy trước hành vi lạng lách có thể gây tai nạn nhưng tự tin vào tay lái của mình rằng hậu quả sẽ không xảy ra -> Lỗi vô ý do quá tự tin."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC4 - Câu 35",
     "Một người đi vào rừng hút thuốc và gạt tàn xuống dưới làm cho tàn thuốc bén vào lá cây khô dẫn đến cháy rừng thì lỗi là gì?",
     ["A. Lỗi vô ý do quá tự tin", "B. Lỗi vô ý do cẩu thả", "C. Lỗi cố ý trực tiếp", "D. Lỗi cố ý gián tiếp"], 1,
     "Do bất cẩn không thấy trước khả năng gây cháy rừng mặc dù phải thấy trước và có thể thấy trước -> Lỗi vô ý do cẩu thả."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC4 - Câu 38",
     "Mình cho bạn vay tiền đến hạn bạn không trả, mình kiện bạn ra tòa, tòa thụ lý giải quyết thì những hình thức thực hiện pháp luật nào được áp dụng trong trường hợp này?",
     ["A. Vận dụng (sử dụng) pháp luật", "B. Chấp hành pháp luật", "C. Áp dụng pháp luật", "D. Đáp án A và C (Mình kiện là Sử dụng/Vận dụng pháp luật; Tòa thụ lý giải quyết là Áp dụng pháp luật)"], 3,
     "Người khởi kiện thực hiện quyền khởi kiện (Sử dụng/Vận dụng pháp luật); Tòa án thụ lý giải quyết vụ án là Áp dụng pháp luật."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC4 - Câu 39",
     "Sinh viên vi phạm quy chế thi bị khiển trách, đó là loại trách nhiệm pháp lý gì?",
     ["A. Trách nhiệm hành chính", "B. Trách nhiệm dân sự", "C. Trách nhiệm kỷ luật", "D. Trách nhiệm hình sự"], 2,
     "Vi phạm nội quy, quy chế của cơ quan, trường học bị xử lý khiển trách, cảnh cáo... là trách nhiệm kỷ luật."),

    ("6. Thực hiện PL, Vi phạm PL & Trách nhiệm pháp lý", "PLDC5 - Câu 26",
     "Mong muốn hậu quả xảy ra khi thực hiện hành vi trái pháp luật là dấu hiệu của loại lỗi nào?",
     ["A. Lỗi vô ý do quá tự tin", "B. Lỗi cố ý gián tiếp", "C. Lỗi cố ý trực tiếp", "D. Lỗi vô ý do cẩu thả"], 2,
     "Nhận thức rõ hành vi là nguy hiểm, thấy trước hậu quả và mong muốn hậu quả xảy ra là lỗi cố ý trực tiếp.")
]

# =========================================================================
# GIAO DIỆN WEB TRẮC NGHIỆM STREAMLIT
# =========================================================================
st.title("⚖️ Hệ thống Ôn luyện Trắc nghiệm Pháp luật Đại cương (EM1170 - HUST)")
st.markdown("Tổng hợp đầy đủ **145 câu hỏi** (sau khi đã gộp các câu trùng lặp từ **hơn 200 câu gốc** trong 9 file đề) thuộc 2 chuyên đề: **Hệ thống chính trị & Bộ máy nhà nước Việt Nam** và **Các vấn đề chung về Pháp luật**.")

# Sidebar cấu hình
with st.sidebar:
    st.header("⚙️ Tùy chọn bài thi")
    topics = ["Tất cả chủ đề"] + sorted(list(set(q[0] for q in QUESTIONS_DB)))
    selected_topic = st.selectbox("Chọn chuyên đề ôn tập:", topics)
    
    mode = st.radio(
        "Chế độ làm bài:",
        ["Kiểm tra ngay từng câu (Ôn tập)", "Nộp bài chấm điểm một lần (Thi thử)"]
    )
    
    shuffle_q = st.checkbox("Trộn ngẫu nhiên thứ tự câu hỏi", value=False)
    if st.button("🔄 Làm mới bài làm"):
        for key in list(st.session_state.keys()):
            if key.startswith("ans_"):
                del st.session_state[key]
        st.rerun()

# Lọc câu hỏi theo chủ đề
filtered_questions = [
    q for q in QUESTIONS_DB
    if selected_topic == "Tất cả chủ đề" or q[0] == selected_topic
]

if shuffle_q:
    if "shuffled_indices" not in st.session_state or st.session_state.get("last_topic") != selected_topic:
        indices = list(range(len(filtered_questions)))
        random.shuffle(indices)
        st.session_state["shuffled_indices"] = indices
        st.session_state["last_topic"] = selected_topic
    display_questions = [filtered_questions[i] for i in st.session_state["shuffled_indices"]]
else:
    display_questions = filtered_questions

st.info(f"📚 Đang hiển thị: **{len(display_questions)} câu hỏi** | Chuyên đề: **{selected_topic}**")
st.divider()

user_answers = {}

for idx, (topic, source, question_text, options, correct_idx, explanation) in enumerate(display_questions):
    st.markdown(f"**Câu {idx + 1}** *(Nguồn: {source})*: {question_text}")
    choice = st.radio(
        "Chọn đáp án:",
        options,
        key=f"ans_{selected_topic}_{idx}",
        index=None,
        label_visibility="collapsed"
    )
    
    if choice is not None:
        chosen_idx = options.index(choice)
        user_answers[idx] = chosen_idx
        
        if mode == "Kiểm tra ngay từng câu (Ôn tập)":
            if chosen_idx == correct_idx:
                st.success(f"✅ Chính xác! Đáp án đúng: **{options[correct_idx]}**\n\n💡 *Giải thích:* {explanation}")
            else:
                st.error(f"❌ Sai rồi! Đáp án đúng phải là: **{options[correct_idx]}**\n\n💡 *Giải thích:* {explanation}")
    st.write("---")

# Nút nộp bài cho chế độ Thi thử
if mode == "Nộp bài chấm điể một lần (Thi thử)":
    if st.button("📝 Nộp bài và Xem kết quả", type="primary", use_container_width=True):
        correct_count = 0
        st.header("📊 Kết quả bài làm")
        for idx, (topic, source, question_text, options, correct_idx, explanation) in enumerate(display_questions):
            u_idx = user_answers.get(idx)
            if u_idx == correct_idx:
                correct_count += 1
                st.success(f"**Câu {idx + 1} ({source}):** Đúng! ({options[correct_idx]})")
            else:
                u_text = options[u_idx] if u_idx is not None else "Chưa chọn"
                st.error(
                    f"**Câu {idx + 1} ({source}):** {question_text}\n\n"
                    f"- Bạn chọn: {u_text}\n"
                    f"- Đáp án đúng: **{options[correct_idx]}**\n"
                    f"- 💡 *Giải thích:* {explanation}"
                )
        
        total = len(display_questions)
        percent = (correct_count / total) * 100 if total > 0 else 0
        st.metric("Tổng điểm của bạn", f"{correct_count} / {total} câu", f"{percent:.1f}%")
        if correct_count == total and total > 0:
            st.balloons()