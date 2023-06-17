from pathlib import Path

import streamlit as st  # pip install streamlit
from PIL import Image  # pip install pillow

# --- PATH SETTINGS ---
THIS_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
ASSETS_DIR = THIS_DIR / "assets"
STYLES_DIR = THIS_DIR / "styles"
CSS_FILE = STYLES_DIR / "main.css"


# --- GENERAL SETTINGS ---
STRIPE_CHECKOUT = "https://buy.stripe.com/bIY5nz8CM7vg2VW6oo"
CONTACT_EMAIL = "consultinghelpglobal@gmail.com"
DEMO_VIDEO = "https://www.youtube.com/watch?v=psuKyBsH1oo"
PRODUCT_NAME = "Business Intuition for Consulting Interviews"
PRODUCT_TAGLINE = "Understand how to think through business cases to ace consulting interviews and advance your career.  🚀"
PRODUCT_DESCRIPTION = """
Break into consulting, learn how to solve common business problems, and advise your clients with confidence:

- **Secure a six figure job right out of college** and double or triple your salary in just a few years. 
- **Get paid to travel the world** and enjoy luxurious perks.
- **Get exposure to many different industries** and job titles to figure out your interests without the negative stigma associated with changing jobs often.
- Have access to an abundance of exit opportunities if you choose to leave.
- Sharpen your business intuition and interpersonal skills.  

**For the price of a cup of coffee, you can take the first step**
"""


def load_css_file(css_file_path):
    with open(css_file_path) as f:
        return st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# --- PAGE CONFIG ---
st.set_page_config(
    page_title=PRODUCT_NAME,
    page_icon=":star:",
    layout="centered",
    initial_sidebar_state="collapsed",
)
load_css_file(CSS_FILE)


# --- MAIN SECTION ---
st.header(PRODUCT_NAME)
st.subheader(PRODUCT_TAGLINE)
left_col, right_col = st.columns((2, 1))
with left_col:
    st.text("")
    st.write(PRODUCT_DESCRIPTION)
    st.markdown(
        f'<a href={STRIPE_CHECKOUT} class="button">👉 Download E-Book</a>',
        unsafe_allow_html=True,
    )
with right_col:
    product_image = Image.open(ASSETS_DIR / "product.png")
    st.image(product_image, width=450)

# --- MOCK INTERVIEW VIDEO ---
st.write("")
st.write("---")
st.subheader(":tv: The Interview")
st.write("**Check out this mock interview released by Bain & Company. Would you be prepared?**")
st.video(DEMO_VIDEO, format="video/mp4", start_time=0)

st.write("""
Wow that was nerve-racking, but kind of interesting right?

You're helping businesses achieve their goals by being analytical. 

Below is another sample case I found that will help you practice your business critical thinking skills. 
""")


# --- Sample Business Case ---
st.write("")
st.write("---")
st.subheader(":raising_hand: Sample Business Case: McKinsey - Beautify")

sample_case = """
**Client Goal**

Our client is Beautify. Beautify has approached McKinsey for help with exploring new ways to approach its customers.

**Situation Description**

Beautify is a global prestige cosmetics company that sells its products mainly inside high-end department stores such as Harrods and Shanghai No. 1. It also has a presence online with specialty retailers like Sephora. Beautify produces a number of makeup, fragrance, and skin care products sold under several different brands.

In department stores, beauty consultants play a critical role with consumers:

* approaching “passive” customers
* demonstrating their knowledge of the products
* actively selling the products
* maintaining a loyal customer base of repeat buyers

These consultants are hired directly by Beautify or through specialist, third-party agencies that find new recruits for a fee. Beautify is then responsible for selecting, training, and paying the consultants. Within Beautify, beauty consultants are managed independently by each brand in each country. For example, this may mean a consultant might be part of the Chanel team in a store. However, consumers are shifting more to online shopping, and too many beauty consultants are left working in empty department stores.

**McKinsey Study**

Beautify’s president and COO engaged McKinsey to help evaluate if training the majority of beauty consultants to use virtual channels to connect with customers could be profitable for the company.
"""
         
question1 = """
Beautify is excited to support its current staff of beauty consultants on the journey to becoming virtual social media-beauty advisors. Consultants would still lead the way in terms of direct consumer engagement and would be expected to maintain and grow a group of clients. They would sell products through their own pages on beautify.com, make appearances at major retail outlets, and be active on all social media platforms.

What possible factors should Beautify consider when shifting this group of employees toward a new set of responsibilities?
"""

question2 = """
One of the key areas that Beautify wants to understand is the reaction of current and potential new customers to the virtual social media-beauty advisors.

Imagine you are a current Beautify customer and you mostly shop at your local department store because you enjoy the high-touch service offered by in-store consultants. What features would make you consider switching to a mostly virtual sales experience?
"""

question3 = """
The discussion about virtual advisors has been energizing, but you’d like to ground the discussion in some analysis. You’ve always found it helpful to frame an investment in terms of how long it will take to turn profitable, such as when incremental revenues are greater than the cost of the project.

You sit down with your teammates from Beautify finance and come up with the following assumptions.

- With advisors, you expect ten percent overall increase in incremental revenue—the team assumes that Beautify will gain new customers who enjoy the experience as well as increased online sales through those engaged, but it will also lose some to other brands that still provide more in-store service. The team assumes this will happen in the first year.
- In that first year, Beautify will invest €50 million in IT, €25 million in training, €50 million in remodeling department store counters, and €25 million in inventory.
- All-in yearly costs associated with a shift to advisors are expected to be €10 million and will start during the first year.
- Beautify’s revenues are €1.3 billion.

How many years would it take until the investment in advisors turns profitable?
"""

st.write(sample_case)

faq = {
    "Question 1": question1,
    "Question 2": question2,
    "Question 3": question3
}
for question, Answer in faq.items():
    with st.expander(question):
        st.write(Answer)

st.subheader("Struggling to answer these questions? Don't know where to start? Need a refresher?")
st.write("""
Join our continuously growing community. New cases are added frequently and will be sent to your email when you purchase.

**Again, for the price of a cup of coffee, you get access to many more cases like these with answers provided.**

**Take the first step to securing the six-figure job you deserve today!**
""")
st.markdown(
        f'<a href={STRIPE_CHECKOUT} class="button">👉 Download E-Book</a>',
        unsafe_allow_html=True,
    )


# --- ABOUT ME ---
st.write("")
st.write("---")
st.subheader("👋 About Me")

about_me = """
You might be wondering who I am so let me tell you a little bit about myself.

I'm currently a consulting manager at a big consulting firm. I've been working here for almost five years now, and it's been quite the journey. 

I studied computer science and math in college, but didn't feel like a traditional coding desk job fit my image of a fulfilling career. Sure, I had a technical background, but what set me apart from my peers was that I also loved to talk to people, enjoyed new, spontaneous experiences, and getting my hands on a lot of different projects rather than dedicating my life to one thing. 

I couldn't relate when my peers were starry eyed about securing that stationary coding job for the rest of their lives. I wanted to travel and see the world, meet people from all different backgrounds and cultures, and overall live an exciting life. 

I had no idea how I was going to accomplish this since everyone told me college would be the best four years of my life and that I would be dead inside as soon as I started a real job. I also had no idea what I wanted to do with my life after college and I thought the best way to find out was to try a lot of things. 

But I was told that switching jobs frequently would cost me my career, so how was I going to try new things if I couldn't switch jobs every few months?

I learned about consulting during my later years of college. I learned that it was a career that allowed me to put my hands into many different jars and figure out what I liked to do instead of commmiting to one thing. It also aligned with what I was passionate about: coding, analytics, and business. It also wasn't like a sales job where you travel around and try to close deals. You have to be analytical and impelement the best solutions. 

It also happens to be a highly lucrative career. 

In my five years doing consulting, I've been to most major cities in the U.S. and a couple of foreign countries. I was able to rack up enough points at hotels to let me live in an upscale hotel in my personal time for more than a month. I had enough flight points to book me six round trip flights from New York City to Los Angeles for free. Sure, there were some sleepless nights when work needed to be done, but it was good for character development and worth it in my opinion.

I would post my travels and accomadations on social media and my friends who were working regular desk jobs would ask how I lived such an exciting life. I was doing everything I've always wanted to do while generating great income. 

That's where I'm at right now at the time of this writing.

By purchasing this book, you will be on my email list. Any updates to this book will be sent your way. You will always have access to any improvements or additional content I add to ensure that you have the resources to be on top of your career.
"""

st.write(about_me)


# --- CONTACT FORM ---
# video tutorial: https://youtu.be/FOULV9Xij_8
st.write("")
st.write("---")
st.subheader(":mailbox: Have A Question? Ask Away!")
contact_form = f"""
<form action="https://formsubmit.co/{CONTACT_EMAIL}" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit" class="button">Send ✉</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)
