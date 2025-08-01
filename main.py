import streamlit as st
from scrape import get_page_content, split_dom_content, clean_body_content, extract_body
from parse import parse_with_ollama


st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL: ")
cleaned_content = ""

if st.button("scrape site"):
    st.write("Scraping the website")
    result = get_page_content(url=url)
    body_content = extract_body(html_content=result)
    cleaned_content = clean_body_content(body_content=body_content)
    st.session_state.dom_content = cleaned_content

with st.expander("View Dom Content"):
    st.text_area("Dom Content", cleaned_content, height=300)


if "dom_content" in st.session_state:
    parse_description = st.text_input("Descrive what you want to parse?")

    if st.button("parse content"):
        if parse_description:
            st.write("parsing content")
            dom_chunks = split_dom_content(dom_content=st.session_state.dom_content)
            parsed_result = parse_with_ollama(dom_chunks, parse_description)
            st.write(parsed_result)