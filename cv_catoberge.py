import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

#############################
# Header
image = Image.open("cato.png")
st.image(image, width=200)

st.write('''
# Cato Berge
### CV
''')

st.markdown("***")

##########################
# Navigation
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark"; style="background-color: #2980B9;>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="#utdanning">Utdanning</a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="#arbeidserfaring">Arbeidserfaring</a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="#kurs">Kurs</a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="#ferdigheter">Ferdigheter</a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="#lenker">Lenker</a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="#nedlastinger">Nedlastinger</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

####################################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b, c):
  col1, col2, col3 = st.columns([1,1,1])
  with col1:
    st.markdown(f"`{a}`")
  with col2:
    st.markdown(f"`{b}`")
  with col3:
    st.markdown(f"`{c}`")

def txt3(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f"`{a}`")
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

######################################
st.markdown("## Kort om", unsafe_allow_html=True)
st.info('''
- Mastergrad samfunnskommunikasjon.
- Erfaring med innholdsproduksjon og internkommunikasjon. Spesielt glad i tekstproduksjon og klarspråk. Liker rutineoppgaver og grave meg ned i detaljer. 
- Erfaring fra sikkerhetsbransjen som kontrollør og konsulent for redusert svinn og økt servicegrad i dagligvare og apotek.
- Glad i og god med foto. Hengiven Fujifilmentusiast. 
- Selvlært datanerd og leker så smått med koding. Er spesielt interessert i datavisualisering gjennom Python, Pandas og Matplotlib.  
''')

st.markdown("***")


st.markdown('''
## Utdanning
''')
txt("*2011-2014*", '''**Mastergrad samfunnskommunikasjon**, Universitet i Agder 
\nStudiet hadde fokus på forståelse og analyse av kommunikasjonen som foregår mellom bedrifter/organisasjoner og samfunnet for øvrig. 
\nMasteroppgave: *Blendet av oljen: en kritisk diskursanalyse av Fædrelandsvennens dekning av næringsklyngen Node*. Karakter: A.''')

txt("*2004-2007*", '''**Bachelorgrad kommunikasjon**, Universitet i Agder 
\nStudiet hadde fokus på tekst- og medieproduksjon, samt analyse av relevante medieprodukter.
''')

st.markdown("***")

st.markdown('''
## Arbeidserfaring''')

txt("*mai 2021-nov. 2021*", '''**Kommunikasjonskonsulent**, Nasjonal kommunikasjonsmyndighet
\n7 måneders vikariat som kommunikasjonskonsulent. 
- Innholdsproduksjon
- Strategisk kommunikasjonsarbeid
- Internkommunikasjon
- Redaktør intranett
- Fungerende pressekontakt ved ferieavvikling
- Kommunikasjonsenhetens- og HR-avdelingens øvrige arbeid
''')

txt("*mai 2020-mar. 2021*", '''**Konsulent**, Pegasus Kontroll og Kompetanse
\nGod hjelp fra tidligere arbeidsgiver etter en tøff korona-vår.
- Revisjoner og oppfølging av disse
- Opplæring og veiledning av nye ansatte
- Kvalitetssikring
''')

txt("*okt. 2019-mai 2020*", '''**Innholdsprodusent**, DrivKraft
\nProduksjon av diverse mediemateriell til hovedsakelig byggevarebransjen.
- Produksjon kataloger
- Tekstarbeid, herunder innholdsproduksjon, språkvask, organisering og oversetting
- Etterbehandling bilder
- Noe fotografering
''')

txt("*jan. 2019-des. 2019*", '''**Kvalitetssikring**, Pegasus Kontroll og Kompetanse
\nKvalitetssikring og kommunikasjon.
- Revisjon av utførte tjenester og oppfølging internt
- Kundedrifter og oppfølging av kunder
- Utarbeidelse av tekst og video til internt bruk
''')

txt("*aug. 2009-des. 2019*", '''**Sivil vekter/kontrollør**, Pegasus Kontroll og Kompetanse
\nSvinnkontroll og serviceforbedring for ulike bransjer og bedrifter.
- Ansvarlig for ambulerende servicevekter
- Butikk-, personal-, alders- og ITV-kontroller, kasserevisjon, tyverikurs med oppfølging, servicemålinger over hele landet
- Instruktøransvar for lærlinger
- Driftsansvar på Amfi Vågsbygd (frem til 01.10.15)
''')

txt("*apr. 2013-apr. 2013*", '''**Assistent**, Universitet i Agder
\nAssistent i forbindelse med 3rd Annual Future Learning Lab Roundtable - Imagine New Learning. 
Koordinering av ulike foredrag og workshops.
''')

txt("*sep. 2012-okt. 2012*", '''**Praksis mastergrad samfunnskommunikasjon**, Innoventus AS
\n6 uker praksis i perioden 17.september til 26.oktober 2012 i forbindelse  med masterstudiet i samfunnskommunikasjon. 
\nHovedoppgavene var:
- å danne seg et inntrykk av det regionale innovasjonssystemet gjennom intervju av gründere og innovasjonsaktører.
- å kartlegge forbedringspotensial i klargjøring av roller innad i innovasjonssystemet.
- annet forefallende arbeid.
''')

txt("*des. 2007-apr. 2009*", '''**Produksjonsmedarbeider**, Osigraf AS
\nProduksjon av Proffpartner-katalogen 2009. 
- Innsamling og organisering av informasjon fra utstyrsprodusenter.
- Enkelt grafisk arbeid og annet forefallende arbeid.
''')

st.markdown("***")

st.markdown('''
## Kurs
''')
txt4("Markedsføring", "**Fundamentals of digital marketing**", "*Google Digital Garage*")
txt4("Python", "**Programmering i Python for viderekomne**", "*Digin/Øystein Grøndahl*")
txt4(" ", "**2021 Complete Python Bootcamp: From Zero to Hero in Python**", "*Jose Portilla(Udemy)*")
txt4("Design thinking", "**Prosessledelse og design tenking**", "*Universitetet i Agder*")
txt4("Skrivekurs", "**Skriv så det selger**", "*Christine Calvert*")

st.markdown("***")

st.markdown('''
## Ferdigheter
''')
txt2("Tekst", "Foto", "IT")
txt2("Service", "Analyse", "Kvalitetssikring")
txt2("Veiledning", "Lightroom", "Sharepoint")
txt2("Python", "Streamlit", "Pandas")

st.markdown("***")

st.markdown('''
## Lenker
''')
txt3("LinkedIn", "https://www.linkedin.com/in/cato-berge-979a0a4b/")
txt3("Twitter", "https://twitter.com/CatoBerge")
txt3("Portefølje foto", "https://adobe.ly/2Xx7FK5")

st.markdown("***")

st.markdown('''
## Nedlastinger
''')

#############################
# Download files
with open("cv_cato_berge.pdf", "rb") as file:
  st.download_button(
    label="Last ned CV",
    data=file,
    file_name="cv_cato_berge.pdf",
    mime="pdf"
  )

with open("cato_berge_vitnemål.pdf", "rb") as file:
  st.download_button(
    label="Last ned vitnemål",
    data=file,
    file_name="cato_berge_vitnemål.pdf",
    mime="pdf"
  )

with open("cato_berge_kurs.zip", "rb") as file:
  st.download_button(
    label="Last ned kursbevis (zip)",
    data=file,
    file_name="cato_berge_kurs.zip",
    mime="zip"
  )
