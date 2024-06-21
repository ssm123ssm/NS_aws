import datetime
import markdown


def creator(info):

    date = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    summary = markdown.markdown(info[0])
    stats_1_1 = markdown.markdown(info[1])
    stats_1_2 = markdown.markdown(info[2])
    stats_2 = markdown.markdown(info[3])
    ratios_1_1 = markdown.markdown(info[4])
    # ratios_1_2 = markdown.markdown(info[5])
    # ratios_2 = markdown.markdown(info[6])
    ratios_3 = "markdown.markdown(info[6])"
    ratios_4 = "markdown.markdown(info[7])"
    ratios_5 = "markdown.markdown(info[8])"
    ratios_6 = "markdown.markdown(info[9])"
    # risks = markdown.markdown(info[10])

    report_template = f"""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap" rel="stylesheet">

<style>
html{{
	background-color:white;
}}

body{{
padding: 30px;
    width: 800;
    margin: auto;
    border: 2px solid #7373a3;
	margin-bottom: 20px;
    margin-top: 20px;
	font-family: 'Montserrat', sans-serif;
}}

h3{{
	color: #56565a;
}}

th, td {{
    border: 1px ridge;
	padding: 7px;
	font-size: small;
}}

.summary{{
    width: 728px;
    text-align: justify;
    margin: auto;
    background-color: #92d6ee45;
    border: 1px solid #4d4e8c;
    padding: 13px;
    margin-top: 48px;
    margin-bottom: 48px;
    font-size: 14px;
    border-radius: 8px;

}}

th{{
    font-size: medium;
}}

table {{
    margin:auto;
	width: 700px;
}}

.risk{{
    background-color: #ffc4c4;
}}

.risks{{
	width: 700;
    text-align: justify;
    margin: auto;
    background-color: #0099b240;
    border: 1px solid #4d4e8c;
    padding: 13px;
    margin-top: 48px;
    margin-bottom: 48px;
    font-size: 13px;
    border-radius: 8px;
    padding-right: 40px;
}}

.stats{{
	margin: auto;
    text-align: inherit;
    width: 700px;
	border: 1px solid;
    padding: inherit;
	font-size: smaller;
}}

.ratios{{
    font-size: smaller;

}}

a{{
    text-decoration: none;
}}
.footer{{
    text-align: center;
    margin-top: 50px;
    font-family: unset;
    letter-spacing: 5px;
    font-size: small;
    color: #4d4e8c;
    background-color: whitesmoke;
    padding: 6px;
	text-decoration:none;

}}

.green {{
    color: #043d89;
    font-weight: 700;
    font-size: 30px;
    margin-bottom:10px
}}

.time{{
    font-family: monospace;
    text-align: center;
    margin-top: -16px;
}}

.b1{{
    width: 300;
    display: inline-block;

}}

.logo{{
    float: right;
    display: inline-block;
    position: relative;
    top: -88px;
    height: 100px;
    left: -14px;
}}
</style>

<div class='b1'>
<h1 id="neurasense-report" class = 'green'>Neurasense Report</h1>
<span class='time'> {date} </span> <br>
<span class='time'> preview version 1.4 alpha </span>

</div>

<img title="logo" alt="neurasense" src="logo.png" class='logo'>

### Summary

<div class='summary'>{summary}</div>



<div class='stats'>{(stats_1_1)}</div>

<br>

<div class='stats'>{(stats_1_2)}</div>

<br>

<div class='stats'>{(stats_2)}</div>

<br>


<div class='ratios'>{(ratios_1_1)}</div>

<br>



<div class='footer'><a href="http://www.neurasense.io">neurasense.io | 2024</a></div>

	"""

    mk = markdown.markdown(str(report_template))

    with open('reports/report_new.html', 'w') as f:
        f.write(mk)
        print('report created')
