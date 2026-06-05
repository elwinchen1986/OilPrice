# -*- coding: utf-8 -*-
import re

def _summarize_tips(tips_text):
    parts = []
    grade_patterns = (
        r'92号汽油(?:上涨|下跌|上调|下调|搁浅|不变)[\d.]+元/升',
        r'95号汽油(?:上涨|下跌|上调|下调|搁浅|不变)[\d.]+元/升',
        r'98号汽油(?:上涨|下跌|上调|下调|搁浅|不变)[\d.]+元/升',
        r'0号柴油(?:上涨|下跌|上调|下调|搁浅|不变)[\d.]+元/升',
    )
    grade_parts = [m.group(0) for p in grade_patterns for m in [re.search(p, tips_text)] if m]
    if grade_parts:
        parts.append('，'.join(grade_parts))
    date_match = re.search(
        r'(?:下次[^，。]{0,10}调整窗口时间为|油价下次调价时间为?|下一个油价调整日期为?)'
        r'\s*(\d{4}年\d{1,2}月\d{1,2}日(?:\d{1,2}[点时:](?:\d{2})?|24时|24点)?)',
        tips_text,
    )
    if date_match:
        parts.append(f'下次调价：{date_match.group(1)}')
    return '，'.join(parts) if parts else tips_text

sample = '2026年6月5日今日油价最新消息：国际油价上涨，WTI原油上涨0.27%，新一轮10个工作日，即92号汽油下跌0.42元/升，95号汽油下跌0.44元/升，0号柴油下跌0.42元/升，下次国内成品油价调整窗口时间为2026年6月18日24时（2026年6月19日0点）。'
print(_summarize_tips(sample))