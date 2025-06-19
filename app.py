import streamlit as st

def get_personality_from_music(music_preference):
    # ここに音楽の好みから性格を診断するロジックを実装します。
    # 例として、簡単なキーワードマッチングを行います。
    if "ロック" in music_preference or "メタル" in music_preference:
        return "情熱的でエネルギッシュな性格です。新しいことに挑戦するのが好きで、リーダーシップを発揮するタイプでしょう。"
    elif "クラシック" in music_preference or "ジャズ" in music_preference:
        return "落ち着きがあり、知的な性格です。物事を深く考える傾向があり、芸術や文化に興味があります。"
    elif "ポップ" in music_preference or "アイドル" in music_preference:
        return "明るく社交的な性格です。人とのコミュニケーションを楽しみ、流行に敏感な一面があります。"
    elif "ヒップホップ" in music_preference or "R&B" in music_preference:
        return "個性的で自己表現豊かな性格です。自分の意見をしっかり持ち、クリエイティブな才能を秘めています。"
    elif "アコースティック" in music_preference or "フォーク" in music_preference:
        return "穏やかで自然体な性格です。内省的で、人との深いつながりを大切にします。"
    else:
        return "あなたの音楽の好みからは、多様な可能性が感じられます。もしかしたら、まだ気づいていない新しい自分を発見できるかもしれませんね。"

st.title("音楽の好みで性格診断アプリ")

st.write("好きな音楽のジャンルを入力してください。あなたの音楽の好みから性格を診断します。")

music_input = st.text_area("あなたの好きな音楽について教えてください（複数可）", "例：クラシック音楽")

if st.button("診断する"):
    if music_input:
        personality = get_personality_from_music(music_input)
        st.subheader("診断結果")
        st.write(personality)
    else:
        st.warning("何か入力してください。")
