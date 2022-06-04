import streamlit as st
import fugashi
from n7 import read_gz, swap_line

st.title("言語崩壊装置")

tagger = fugashi.Tagger()
ref = read_gz("lex.csv.gz")

st.write("""この言語崩壊装置は[ナマケモノ、大根を泳ぐ](https://shonenjumpplus.com/episode/3270296674372939104)と[ABA氏のツイート](https://twitter.com/abagames/status/1530711200329519104)を見て、なにか実装できないかと思って作っちゃいました。仕組みは基本的に[OulipoのS+7](https://ja.wikipedia.org/wiki/%E3%82%A6%E3%83%AA%E3%83%9D#:~:text=%E3%80%8C-,%E8%AA%9E%E5%BD%99%E7%9A%84%E5%B9%B3%E8%A1%8C%E7%A7%BB%E5%8B%95,-%E3%80%8D%E3%81%A8%E3%82%82%E5%91%BC%E3%81%B0%E3%82%8C%E3%82%8B%E3%80%82%E3%81%BE%E3%81%9A)と同じで、対象となる単語を辞書で引き、X項目後ろの単語に置き換えます。

文章を程よく崩壊させるために、置き換えは同じ品詞の単語に限定していますが、その結果品詞が特徴的なもの（「大きな」など）が崩壊されないことがあります。また普通名詞は「一般社団法人」のような複合名詞にはならず、複合動詞が多いなど、クセが色々あります。

ソースは[こちら](https://github.com/polm/language-disruptor)。
""")

text = st.text_area("崩壊させる文章を入力してください", value="バベルの塔は、旧約聖書の「創世記」中に登場する巨大な塔。")

if st.button("大根を泳ぐ"):
    st.write(swap_line(tagger, ref, text))

