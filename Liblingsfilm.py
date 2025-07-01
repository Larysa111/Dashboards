import streamlit as st
TITLE = "The Borgias"
POSTER_URL = r"C:\Users\11kuc\OneDrive\Desktop\Bordja.jpg"
YOUTUBE_INTRO = "https://youtu.be/bQZ9CHtImDM"
EMMY_AWARD = r"C:\Users\11kuc\Schulung\project _ins\EmmyAward.jpg"

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

with st.container():
    col_poster, col_title = st.columns([1,2], gap = "large")
    with col_poster:
        st.image(POSTER_URL, use_container_width = True)
    with col_title:
        st.title(f"{TITLE}")
        st.caption  (INFO["Year"] + " | " + INFO["Country"] + " | " + INFO["Duration"] )

        m1, m2, m3 = st.columns(3)
        m1.metric("IMDb rating", INFO ["IMDb rating"], None)
        m2.metric("Seasons", INFO["Seasons"])
        m3.metric("Episodes", INFO["Episodes"])

        st.write(SUMMARY)

overview_tab, cast_tab, media_tab = st.tabs(["Overview", "Main Cast", "Media"])

with  overview_tab:
    st.subheader("Story development")  
    st.write(
        """
        In the “eternal” city, few people like the Borgia family — an Italian family with Spanish roots — they have many enemies, 
        but after the death of Pope Innocent VIII, through bribery and exposés, the Holy See is taken over by Rodrigo Borgia, 
        who takes the name Alexander VI. 
        At this time, Rodrigo's enemy, Cardinal Giuliano della Rovere, travels through the Italian states and France, 
        seeking allies in the fight against the Borgias. He manages to persuade the French king, Charles VIII, 
        to depose the pope in exchange for recognition as king of Naples. The French army arrives in Rome, 
        and the pope meets with the king.
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

    



