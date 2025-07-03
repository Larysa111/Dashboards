import streamlit as st
TITLE = "The Borgias"
POSTER_URL = "https://i.imgur.com/9dnJNbh.jpeg"
YOUTUBE_INTRO = "https://youtu.be/bQZ9CHtImDM"
EMMY_AWARD = "https://i.imgur.com/DsRXjaz.jpeg"
custom_css = """
<style>
.stApp {
    margin: 0;
    padding: 0;
    background-image: url('https://victortravelblog.com/wp-content/uploads/2024/10/caspar_andriaans_van_wittel_-the_castel_sant_angelo_from_the_south-1024x770.jpg');
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
}
.stApp::before {
    content: "";
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    background-color: rgba(255,255,255,0.5);  /* ← здесь регулируется "осветление" */
    z-index: 0;
}
.main-block {
    position: relative;
    z-index: 1;  /* чтобы быть поверх осветлителя */
    background-color: rgba(0, 0, 0, 0.5);
    padding: 2rem;
    border-radius: 10px;
    color: white; /* Текст внутри этого блока останется белым, так как фон темный */
}

/* Этот класс .main в вашем коде не используется напрямую в HTML-разметке,
   но если бы использовался, то его текст тоже был бы белым. */
.main {
    background-color: rgba(0, 0, 0, 0.5);
    padding: 2rem;
    border-radius: 10px;
    color: white; /* Текст внутри этого блока останется белым */
}

/* Исправленные и добавленные стили для общего текста */
/* Используем универсальный селектор * или более специфичные для текста */
* { /* Применяем ко всем элементам, если не переопределено */
    color: #1a1a1a; /* Очень темно-серый, почти черный */
}

/* Можно также применить к конкретным элементам, если нужно */
p {
    color: #000000; /* Чисто черный для всех параграфов */
}
h1, h2, h3, h4, h5, h6 {
    color: #000000; /* Чисто черный для всех заголовков */
}
/* Если хотите, чтобы текст в сайдбаре тоже был темным,
   можете добавить стили для элементов внутри .st-emotion-cache-1ldf03x (класс сайдбара Streamlit) */
.st-emotion-cache-1ldf03x * { /* Это пример селектора для сайдбара, может меняться в разных версиях Streamlit */
    color: #1a1a1a;
}
</style>
"""

# Добавляем CSS в страницу
st.markdown(custom_css, unsafe_allow_html=True)

# with st.container():
#     st.markdown('<div class="main-block">', unsafe_allow_html=True)


hide_streamlit_style = """
    <style>
        header {
        display: none !important;
    }
        #MainMenu {
        visibility: hidden;
        height: 0px; /* Убеждаемся, что не занимает места */
        overflow: hidden; /* Предотвращаем любые артефакты, если visibility:hidden оставляет их */
    }
        footer {
        visibility: hidden;
        height: 0px; /* Убеждаемся, что не занимает места */
    }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)        
      

INFO = {
    "Year": "2011",
    "Country": "Ungarn, Irland, Kanada, USA",
    "Seasons": 3,
    "Episodes": 29,
    "Duration": "about 50 Min./Episode",
    "IMDb rating": "7.9 / 10",
    "Amazon rating": "6.6 / 10"
}


CAST_MAIN = [
    "Rodrigo Borgia - Jeremy Irons",
    "Cesare Borgia - François Arnaud",
    "Lucrezia Borgia - Holliday Grainger",
    "Huang Borgia - David Oakes",
    "Vanocca - Joanne Whalley"
]

SUMMARY = """
    In the “eternal” city, few people like the Borgia family — an Italian family with Spanish roots — they have many enemies, 
        but after the death of Pope Innocent VIII, through bribery and exposés, the Holy See is taken over by Rodrigo Borgia, 
        who takes the name Alexander VI. 
        At this time, Rodrigo's enemy, Cardinal Giuliano della Rovere, travels through the Italian states and France, 
        seeking allies in the fight against the Borgias. He manages to persuade the French king, Charles VIII, 
        to depose the pope in exchange for recognition as king of Naples. The French army arrives in Rome, 
        and the pope meets with the king.
    """

with st.container():
    col_poster, col_title = st.columns([4,3], gap = "large")
    with col_poster:
        st.image(POSTER_URL, width=450)
    with col_title:
        st.title(f"{TITLE}")
        st.caption (INFO["Year"] + " | " + INFO["Country"] + " | " + INFO["Duration"] )

        m1, m2, m3 = st.columns(3)
        m1.metric("IMDb rating", INFO ["IMDb rating"], None)
        m2.metric("Seasons", INFO["Seasons"])
        m3.metric("Episodes", INFO["Episodes"])

        st.write(SUMMARY)

overview_tab, cast_tab, media_tab = st.tabs(["Overview", "Main Cast", "Media"])

with overview_tab:
    st.subheader("Story development")  
    st.write(
        """
        The second half of the 15th century was a turning point in the life of Rome and Catholicism as a whole.
    Rodrigo Borgia, first thanks to family connections, then using his cunning mind and diplomatic skills, 
    managed to obtain the title of Pope. The man began to rule the possessions entrusted to him with an iron fist.
    Those who were dissatisfied and openly opposed him could be subjected to persecution and painful execution,
    and their property would go to the religious leader. Behind-the-scenes struggles were no less effective than open negotiations and business visits. 
    The threat from the French monarchs, who wanted to obtain hereditary lands, was met with a worthy response from the hero. 
    Numerous advantageous alliances and influential acquaintances invariably helped him turn the situation to his advantage.
    The new Pope also became famous as a very dissolute man who loved fornication and illicit relationships.He had several sons, 
    each of whom received enough privileges to rise in status. Cesare achieved the most impressive successes, 
    leading the army in effective maneuvers and operations. Rodrigo's insatiability knew no bounds; even in his old age, 
    he continued to expand his possessions, weaving intrigues and conspiracies.
        """
    )   
    with st.expander("🏆 Nominations and Awards"):
        col_text, col_image = st.columns([1,2])

        with col_text:
            st.markdown("""      
            The Borgias series received several awards and nominations, including an Emmy Award for Outstanding Music Composition for a Drama Series. 
            Jeremy Irons, who played the lead role, was nominated for an Emmy Award for Outstanding Lead Actor in a Drama Series for his role in The Borgias. 
            In total, the series was nominated for 10 Emmy Awards. In addition, the series won the Audience Choice Award at the 37th Montreal International Festival. 
            """)

        with col_image:
            st.image(EMMY_AWARD, width = 150, caption = "Emmy Award")

with cast_tab:
    st.subheader("Cast - Main roles")
    st.write("\n".join([f"- {member}" for member in CAST_MAIN]))

with media_tab:
    st.subheader("Series intro(Video)")
    st.video(YOUTUBE_INTRO)


with st.sidebar:
    st.header("📈 statistics")    
    st.metric("IMDb rating", INFO["IMDb rating"])

    st.header("🔗 Links")
    st.markdown(
        """
        * [🎬 IMDb-website](https://www.imdb.com/title/tt1582457/)
        * [📚 Wikipedie-article](https://en.wikipedia.org/wiki/The_Borgias_(2011_TV_series))
        """
    )
st.markdown('</div>', unsafe_allow_html=True)



