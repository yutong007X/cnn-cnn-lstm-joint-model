import string
import pickle


class Index(object):
    def __init__(self):
        self.key2idx = {}
        self.idx2key = []

    def add(self, key):
        if key not in self.key2idx:
            self.key2idx[key] = len(self.idx2key)
            self.idx2key.append(key)
        return self.key2idx[key]

    def __getitem__(self, key):
        if isinstance(key, str):
            return self.key2idx[key]
        if isinstance(key, int):
            return self.idx2key[key]

    def __len__(self):
        return len(self.idx2key)

    def save(self, f):
        with open(f, 'wt', encoding='utf-8') as fout:
            for index, key in enumerate(self.idx2key):
                fout.write(key + '\t' + str(index) + '\n')

    def load(self, f):
        with open(f, 'rt', encoding='utf-8') as fin:
            for line in fin:
                line = line.strip()
                if not line:
                    continue
                key = line.split()[0]
                self.add(key)


class Wordset(Index):
    def __init__(self):
        super().__init__()
        #char_set = ("")
        #char_set = ('拆乘废￥乡归帘香吊穿迟叠畴瓶亮宿秀！⑴畅⑵洗⑶蜂鸣尾跌搅拌养浏览~奥膺碰撞犹雄狮扼咽')
        char_set = ('sdfdsacb前，人类就发现动物体带电的事实并利用鳐所生治疗精神病在智超市货架上不乏中国商品其纺织、服装五金厨房具鞋箱包占了很大额玻璃管温计是应最广泛一种结构简单使方便准确高价格低廉继')
        #char_set = ('多年前，人类就发现动物体带电的事实并利用鳐所生治疗精神病在智超市货架上不乏中国商品其纺织、服装五金厨房具鞋箱包占了很大份额玻璃管温度计是应最广泛一种结构简单使方便准确高价格低廉继器控制系统般由主令接触和导线等部分组成,逻辑功能传来完比如时间有相且作与磁关条形码阅读也称为扫描枪于取含信息设备将个经典理论量子化原因要借着概率福析解质或粒属性感数据库cnseor力敏热工流位移速光学医气湿射字特殊声波变送容式压尺寸转霍尔血觉水紫外避雷噪音执行荷重角偶齿轮涡置激脉向燃露点浊粘指纹地震加铂阻陀螺近红图像烟ph象笔迹防爆频风差振铑矩液舌簧纤毒密酸微语纳米编伐倾斜距深幕色浓离颜仪表监视软件IC路可无网络技术型交叉科军民两战略以家安全环境通灾害预测卫造业城建领域又及识别（RFD）世纪8代展起新兴自项号过空耦合场递达到目师该帮助各院校立课程旦教育知仅毕果得扩同会从适研究出版序源换机械拨定六元冷却扇车辆直影响散效进而稳调整输供较求它值范围内下正常晶宝石d3+：YAG都模选择括次连续待还增极限操非暗盒筑修施必须辅保障渡护后MOS摄细被素(Paivxl)t当今务“”处凭卓越灵活日益颖消费普蓄池基平衡根端入面法强B那么垂即之产势VH小腐采锈钢材料蚀介对道布畸旋充此游侧配段若情况明推荐长5满足述节标专至6伏二回负检验漏身提插座头靠档开顾名思义词释启闭互补站太阳阵逆缆支撑给载沥青胶玛蹄脂m填滑粉云母棉煤灰LE灯丝叫柱往照积需透镜降°未灭弧罩似彩矫偏期片既艺俗念混跃迁状态跳更遍意途银款录航天险柜按浆瞬快书馆静投油冶药排《》7社昱著籍缸伺杠块运佳优-扭；列革命见放冲浪涌止击损坏yu文氧半本算芯存引资姿参考轴够飞横滚翻这探随许偿复栅W谐倍受拉曼双吸收饱聚焦束纵但腔耗枢轻食北京9月4门委员办央级刷固绕叶壳零筒切停做规则说某刻言去任耐塑木轨联几夹板〜缝胀缩弦急讯星救警船舶.总U集薄膜厚陶瓷铜碳锗铁详绍注第三熟饶约泵浦样严匹k裂均匀宽缘故阈稀土丰富荧谱摩擦紧页记他候问题圆弱打础另显示柔画申请证贸易者决纠纷权派局授托律隔凑仓储先沿企营跟踪获订始购付每步您尽堆溴碘铊K窗口远杆锥层拖背孔荡颗隧草坪绿杂志创刊华共团公司四十七报异熔免拟针g隶遥里氢氮氦绝顶底谓禁清兼侦查恒侵镍镉亚墨海绵筛钠钾溶印滤只把硬已遵守际符NXf蓝牙持/壁挂诸案暖洁净厂楼宇想街干谈串抗Z永励陈客我队纯维媒播忽=q≈*^断英b豪汽升椅床伸末们旧观努初些看何区呢判碍径～汇户然再套铅凝失附贴馈卡才签竹铝Q延寿·致J－龙骨亦硅手劣居住舒健康钮界．嵌逐携斩割壤弗黄腊碱涂改氯乙烯树真没珠悬浮w斥试评湓淋落磨好炮弹武汉邮少走弯劳享财征隙轭反j周棒刨焊剂挤℃焙烤镀良泄泡肉眼察:–张堵融T桥阀枕依驳纽抽屉否截甚兆欧摇减驱马②盘政府%白暴老除早挥独拼写误措辐z幅漫槽炸危蒸巨巡阐右责键策—匮职缺招锯德阿斯蒂省掺③④扰济伞贵铒室锌剩余督章历史趋练习雪崩衰抖孤景缠隐钥协议献…凤裴丽宁纲裹谁买？售乃循曲拥齐钞娱乐麻舞台黑综虑久毫糊兵核短瓦μ亨繁奈奎副边圈宣告审宜虹矿拔淬铸喷球"庭宅雕辊钻左烦恼仍纸滞难喜卖穷阶址×脑抄勤寻找膨心唯恰答怎戏呼炼山抢火牌帧划①Ⅱ衔坐魁克万听凹毛罗氏礼折锡锆钛钡首例拓陆终握践勇敢吃螃蟹梁笼迅猛春剧破冒屋伤乎认缓善己询洞拦圣伦河拿东港塞兰渊朗烧灌碎浸涉凉覆盖尘儿童刘君女江西泰博士污洋井罐封脚染喇锁兽皮汁渗贮让掘皿陷美卷演添译味稠仿退迷你批吻勒剖岩坡莫辙岔映尖帽官掌胜遇赋呈留秒埋扣垫眩锅炉廊栈翘倒顺承百古漆碴砂乳泥替阂硼酶酪氨胺歧蛋允酰αω羧βγ烷醇δ族芳烃丙甲盐酯羟腈酐噁唑啉嗪酮拆乘废￥乡归帘香吊穿迟叠畴瓶亮宿秀！⑴畅⑵洗⑶蜂鸣尾跌搅拌养浏览~奥膺碰撞犹雄狮扼咽喉铬钨胞矢宙锂逸函脱垒疏诊卤泽突闸刚橙扬ō桌匣洲坚农村牧吨藏畜讲辨夫屏撤巧朝虚困迈川Φ逊阴肖λε<悉培楚潜遮千厘销橡硫衬尤冻敷鲜冰衣宏贯翼训南威')
        for char in char_set:
            self.add(char)
        self.add("<pad>")
        self.add("<unk>")

    @staticmethod
    def type(char):
        if char in string.digits:
            return "Digits"
        if char in string.ascii_lowercase:
            return "Lower Case"
        if char in string.ascii_uppercase:
            return "Upper Case"
        if char in string.punctuation:
            return "Punctuation"
        return "Other"

    def __getitem__(self, key):
        if isinstance(key, str) and key not in self.key2idx:
            return self.key2idx["<unk>"]
        return super().__getitem__(key)




class Charset(Index):
    def __init__(self):
        super().__init__()
        for char in string.printable[0:-6]:#所有的字母加符号
            self.add(char)
        self.add("<pad>")
        self.add("<unk>")

    @staticmethod
    def type(char):
        if char in string.digits:
            return "Digits"
        if char in string.ascii_lowercase:
            return "Lower Case"
        if char in string.ascii_uppercase:
            return "Upper Case"
        if char in string.punctuation:
            return "Punctuation"
        return "Other"

    def __getitem__(self, key):
        if isinstance(key, str) and key not in self.key2idx:
            return self.key2idx["<unk>"]
        return super().__getitem__(key)


class Vocabulary(Index):
    def __init__(self):
        super().__init__()
        self.add("<pad>")
        self.add("<unk>")

    def __getitem__(self, key):
        if isinstance(key, str) and key not in self.key2idx:
            return self.key2idx["<unk>"]
        return super().__getitem__(key)


def prepare_sequence(seq, to_idx):
    return [to_idx[key] for key in seq]


def save(obj, path):
    with open(path, 'wb') as f:
        pickle.dump(obj, f)


def load(path):
    with open(path, 'rb') as f:
        return pickle.load(f)


def time_display(s):
    d = s // (3600*24)
    s -= d * (3600*24)
    h = s // 3600
    s -= h * 3600
    m = s // 60
    s -= m * 60
    str_time = "{:1d}d ".format(int(d)) if d else "   "
    return str_time + "{:0>2d}:{:0>2d}:{:0>2d}".format(int(h), int(m), int(s))
