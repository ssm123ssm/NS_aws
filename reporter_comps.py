class component:
    def __init__(self):

        self.temp = """

        <instructions>

        All of the following ratios should be extracted/calculated for the latest year, for the COMPANY AND THR GROUP seperately. Mention how relevent financial parameters were extracted/calculated with exact page number and exerpt in a footnote.
        Output a should be the HTML code of the table and the footnote.

        </instructions>

        <tasks>

        calculate asset turnover ratio and show the result in the table. The formula for asset turnover ratio is Revenue / Total Assets. The result should be shown in the table with the name of the ratio, formula and the calculated value. Include a column to show how the value was calculated.  Do not contain any additional thing in the answer apart from the table.

        Calculate inventory turnover ratio and show the result in the table. The formula for inventory turnover ratio is Cost of Goods Sold / Inventory. The result should be shown in the table with the name of the ratio, formula and the calculated value. Include a column to show how the value was calculated.  Do not contain any additional thing in the answer apart from the table.

        </tasks>

        """

        self.ratios_6 = """

        <instructions>

        All of the following ratios should be extracted/calculated for the latest year, for the COMPANY AND THR GROUP seperately. Mention how relevent financial parameters were extracted/calculated with exact page number and exerpt in a footnote.
        Output a should be the HTML code of the table and the footnote.

        </instructions>

        <tasks>

        calculate asset turnover ratio and show the result in the table. The formula for asset turnover ratio is Revenue / Total Assets. The result should be shown in the table with the name of the ratio, formula and the calculated value. Include a column to show how the value was calculated.  

        Calculate inventory turnover ratio and show the result in the table. The formula for inventory turnover ratio is Cost of Goods Sold / Inventory. The result should be shown in the table with the name of the ratio, formula and the calculated value. Include a column to show how the value was calculated.  

        </tasks>

        """

        self.ratios_5 = """

        <instructions>

        All of the following ratios should be extracted/calculated for the latest year, for the COMPANY AND THR GROUP seperately. Mention how relevent financial parameters were extracted/calculated with exact page number and exerpt in a footnote.
        Output a should be the HTML code of the table and the footnote.

        </instructions>

        <tasks>

        Calculate liquidity ratio and show the result in the table. The formula for liquidity ratio is Current Assets / Current Liabilities. The result should be shown in the table with the name of the ratio, formula and the calculated value. Include a column to show how the value was calculated.  

        Calculate leverage ratio and show the result in the table. The formula for leverage ratio is Total Liabilities / Total Assets. The result should be shown in the table with the name of the ratio, formula and the calculated value.  Include a column to show how the value was calculated. 

        </tasks>

        """

        self.ratios_4 = """

        <instructions>

        All of the following ratios should be extracted/calculated for the latest year, for the COMPANY AND THR GROUP seperately. Mention how relevent financial parameters were extracted/calculated with exact page number and exerpt in a footnote.
        Output a should be the HTML code of the table and the footnote.

        </instructions>

        <tasks>

        calculate earnings per share and show the result in the table. The formula for earnings per share is Net Income / Number of Shares. The result should be shown in the table with the name of the ratio, formula and the calculated value. Include a column to show how the value was calculated.  

        Calculate profit margin and show the result in the table. The formula for profit margin is Net Income / Revenue. The result should be shown in the table with the name of the ratio, formula and the calculated value. Include a column to show how the value was calculated. 

        </tasks>

        """

        self.ratios_3 = """

        <instructions>

        All of the following ratios should be extracted/calculated for the latest year, for the COMPANY AND THR GROUP seperately. Mention how relevent financial parameters were extracted/calculated with exact page number and exerpt in a footnote.
        Output a should be the HTML code of the table and the footnote.

        </instructions>

        <tasks>

        calculate the return on assets ratio and show the result in the table. The formula for return on assets ratio is Net Income / Total Assets. The result should be shown in the table with the name of the ratio, formula and the calculated value. Include a column to show how the value was calculated.  

        calculate the current ratio and show the result in the table. The formula for current ratio is Current Assets / Current Liabilities. The result should be shown in the table with the name of the ratio, formula and the calculated value. Include a column to show how the value was calculated.  

        </tasks>

        """

        self.ratios_2 = """

        <instructions>

        All of the following ratios should be extracted/calculated for the latest year, for the COMPANY AND THR GROUP seperately ONLY using the context provided. Mention how relevent financial parameters were extracted/calculated with exact page number and exerpt in a footnote. If the necessary parameters are not in the context, keep the cell empty and mention that in the footnote.
        Output a should be the HTML code of the table and the footnote.

        </instructions>

        <tasks>

         calculate the return on equity ratio and show the result in the table. The formula for return on equity ratio is Net Profit / Total Equity. The result should be shown in the table with the name of the ratio, formula and the calculated value for the latest year. Include a column to show how the value was calculated.   Mention how net profit was extracted/calculated with exact page number and exerpt. Do not contain any preambles in the answer apart from the table and the footnote.

        calculate the debt to equity ratio and show the result in the table. The formula for debt to equity ratio is Total Liabilities / Total Equity. Total liabilities in a company's financial statement constitute accounts payable, short-term loans or notes payable, accrued expenses such as salaries, taxes, and interest, unearned or deferred revenue, current portion of long-term debt, long-term debt or bonds payable, deferred tax liabilities, pension obligations, lease liabilities, contingent liabilities, provisions for warranties, lawsuits, or environmental liabilities. The result should be shown in the table with the name of the ratio, formula and the calculated value. Include a column to show how the value was calculated. Do not contain any preambles in the answer apart from the table and the footnote.  

        </tasks>

        """

        self.ratios_1_1 = """

        <instructions>

        All of the following ratios should be extracted/calculated for the latest year, for the COMPANY AND THR GROUP seperately ONLY using the context provided. Mention how relevent financial parameters were extracted/calculated with exact page number and exerpt in a footnote. If the necessary parameters are not in the context, keep the cell empty and mention that in the footnote.
        Output a should be the HTML code of the table and the footnote.

        </instructions>

        <tasks>

       calculate the Quick ratio and show the result in the table. The formula for Quick ratio is (Current Assets - Inventory) / Current Liabilities. Current liabilities should include trade and other payables, Current income tax liabilities, current lease liabilities and any other relevant parameters. The current liabilities in a company's financial statement typically include accounts payable, short-term loans or notes payable, accrued expenses such as salaries, taxes, and interest, unearned or deferred revenue, and the current portion of long-term debt. The result should be shown in the table with the name of the ratio, formula and the calculated value. Include a column to show how the value was calculated. Do not contain any preambles in the answer apart from the table and the footnote.

       </tasks>
       

        """

        self.ratios_1_2 = """

        <instructions>

        All of the following ratios should be extracted/calculated for the latest year, for the COMPANY AND THR GROUP seperately ONLY using the context provided. Mention how relevent financial parameters were extracted/calculated with exact page number and exerpt in a footnote. If the necessary parameters are not in the context, keep the cell empty and mention that in the footnote.
        Output a should be the HTML code of the table and the footnote.

        </instructions>

        <tasks>

       Calculate cash ratio and show the result in the table. The formula for cash ratio is Cash / Current Liabilities. Current liabilities should include trade and other payables, Current income tax liabilities, current lease liabilities and any other relevant parameters. The current liabilities in a company's financial statement typically include accounts payable, short-term loans or notes payable, accrued expenses such as salaries, taxes, and interest, unearned or deferred revenue, and the current portion of long-term debt. The result should be shown in the table with the name of the ratio, formula and the calculated value. Include a column to show how the value was calculated. Do not contain any preambles in the answer apart from the table and the footnote.  

       </tasks>
       

        """

        self.tester_template_ratios = """

        All of the following ratios should be calculated for the year 2023. Output a should be the HTML code of the table.

       calculate the Quick ratio and show the result in the table. The formula for Quick ratio is (Current Assets - Inventory) / Current Liabilities. The result should be shown in the table with the name of the ratio, formula and the calculated value. Include a column to show how the value was calculated. Do not contain any additional thing in the answer apart from the table.

       Calculate cash ratio and show the result in the table. The formula for cash ratio is Cash / Current Liabilities. The result should be shown in the table with the name of the ratio, formula and the calculated value. Include a column to show how the value was calculated.  Do not contain any additional thing in the answer apart from the table.

       calculate the debt to equity ratio and show the result in the table. The formula for debt to equity ratio is Total Liabilities / Total Equity. The result should be shown in the table with the name of the ratio, formula and the calculated value. Include a column to show how the value was calculated.  Do not contain any additional thing in the answer apart from the table.

         calculate the return on equity ratio and show the result in the table. The formula for return on equity ratio is Net Income / Total Equity. The result should be shown in the table with the name of the ratio, formula and the calculated value. Include a column to show how the value was calculated.  Do not contain any additional thing in the answer apart from the table.

            calculate the return on assets ratio and show the result in the table. The formula for return on assets ratio is Net Income / Total Assets. The result should be shown in the table with the name of the ratio, formula and the calculated value. Include a column to show how the value was calculated.  Do not contain any additional thing in the answer apart from the table.

            calculate the current ratio and show the result in the table. The formula for current ratio is Current Assets / Current Liabilities. The result should be shown in the table with the name of the ratio, formula and the calculated value. Include a column to show how the value was calculated.  Do not contain any additional thing in the answer apart from the table.

            calculate earnings per share and show the result in the table. The formula for earnings per share is Net Income / Number of Shares. The result should be shown in the table with the name of the ratio, formula and the calculated value. Include a column to show how the value was calculated.  Do not contain any additional thing in the answer apart from the table.

            Calculate profit margin and show the result in the table. The formula for profit margin is Net Income / Revenue. The result should be shown in the table with the name of the ratio, formula and the calculated value. Include a column to show how the value was calculated.  Do not contain any additional thing in the answer apart from the table.

            Calculate liquidity ratio and show the result in the table. The formula for liquidity ratio is Current Assets / Current Liabilities. The result should be shown in the table with the name of the ratio, formula and the calculated value. Include a column to show how the value was calculated.  Do not contain any additional thing in the answer apart from the table.

            Calculate leverage ratio and show the result in the table. The formula for leverage ratio is Total Liabilities / Total Assets. The result should be shown in the table with the name of the ratio, formula and the calculated value.  Include a column to show how the value was calculated. Do not contain any additional thing in the answer apart from the table.

            calculate asset turnover ratio and show the result in the table. The formula for asset turnover ratio is Revenue / Total Assets. The result should be shown in the table with the name of the ratio, formula and the calculated value. Include a column to show how the value was calculated.  Do not contain any additional thing in the answer apart from the table.

            Calculate inventory turnover ratio and show the result in the table. The formula for inventory turnover ratio is Cost of Goods Sold / Inventory. The result should be shown in the table with the name of the ratio, formula and the calculated value. Include a column to show how the value was calculated.  Do not contain any additional thing in the answer apart from the table.
        
        """

        self.tester_template_balance_sheet_1_1 = """

            <instructions>

            All of the following parameters should be extracted/calculated for the latest year FOR THE COMPANY and the GROUP seperately, using the sections named Financial Statement or similar. If several values are given in the context, select the total value relevant to the main company and the group, the annual report is on. The output should be HTML code of the tables with appropriate headings. At the enad of each table, include a paragraph which critically evaluates the paramerers with the previous year. Properly format this paragraph in HTML and include sources, section name, page number as references as footnotes. Do not include any other thing apart from the correct HTML code. There should be a table per task, with a critical evaluation paragraph for each table. NEVER provide preambles like "Here is the analysis you asked...". ONLY provide the required tables/paragraphs in HTML.

            </instructions>

            <tasks>

            1. All the available current and non-current assets. Do not miss any of the data. Mention the unit of price. The accuracy of this is crucial. The table should contain the name of the parameter, the year and the value. Do not contain any additional thing in the answer apart from the correct HTML code for the table and the critical evaluation paragraph with references. The data provided may contain financial details for the company, the group and for several years. Make sure to extract the data for them seperately for the latest year, and for critical evaluation, compare the data with the previous year.

            </tasks>

        """

        self.tester_template_balance_sheet_1_2 = """

            <instructions>

            All of the following parameters should be extracted/calculated for the latest year FOR THE COMPANY and the GROUP seperately, using the sections named Financial Statement or similar. If several values are given in the context, select the total value relevant to the main company and the group, the annual report is on. The output should be HTML code of the tables with appropriate headings. At the enad of each table, include a paragraph which critically evaluates the paramerers with the previous year. Properly format this paragraph in HTML and include sources, section name, page number as references as footnotes. Do not include any other thing apart from the correct HTML code. There should be tables per task, with a critical evaluation paragraph for each table. NEVER provide preambles like "Here is the analysis you asked...". ONLY provide the required tables/paragraphs in HTML.

            </instructions>

            <tasks>

            1. All the available current and non-current liabilities including employee benefit obligations, Deferred tax liabilities, lease liabilities, Trade and other payables, Current income tax liabilities. Do not miss any of the data. Mention the unit of price. The accuracy of this is crucial. The table should contain the name of the parameter, the year and the value. Do not contain any additional thing in the answer apart from the correct HTML code for the table and the critical evaluation paragraph with references. The data provided may contain financial details for the company, the group and for several years. Make sure to extract the data for them seperately for the latest year, and for critical evaluation, compare the data with the previous year.

            </tasks>

        """

        self.tester_template_balance_sheet_2 = """

            <instructions>

            All of the following parameters should be extracted/calculated for the latest year FOR THE COMPANY and the GROUP seperately, using the sections named Financial Statement or similar. If several values are given in the context, select the total value relevant to the main company and the group, the annual report is on. The output should be HTML code of the tables with appropriate headings. At the enad of each table, include a paragraph which critically evaluates the paramerers with the previous year. Properly format this paragraph in HTML and include sources, section name, page number as references as footnotes. Do not include any other thing apart from the correct HTML code. There should be TWO tables per task, with a critical evaluation paragraph for each table.

            </instructions>

            <tasks>

            1. All the available equity. Do not miss any of the data. Mention the unit of price. The accuracy of this is crucial. The table should contain the name of the parameter, the year and the value. Do not contain any additional thing in the answer apart from the correct HTML code for the table and the critical evaluation paragraph with references. The data provided may contain financial details for the company, the group and for several years. Make sure to extract the data for them seperately for the latest year, and for critical evaluation, compare the data with the previous year.

            2. All the available revenue, direct costs associated with revenue to identify gross profit, operating expenses, and net income. Calculate gross profit margin, operating profit margin, and net profit margin. Do not miss any of the data. Mention the unit of price. The accuracy of this is crucial. The table should contain the name of the parameter, the year and the value. Do not contain any additional thing in the answer apart from the correct HTML code for the table and the critical evaluation paragraph with references. The data provided may contain financial details for the company, the group and for several years. Make sure to extract the data for them seperately for the latest year, and for critical evaluation, compare the data with the previous year.

            </tasks>

             NEVER provide preambles like "Here is the analysis you asked...". ONLY provide the required tables/paragraphs in HTML.

             <output>
             </output>

        """

        self.summary = "Generate a concise summary about this company in a critical stand-point. The summary should contain detials on What is this business, what are the areas that they are established in, what are their products and their market position. There should be a comparsion of key financial parameters with the previous year. The facts must be extracted from the given data and they must be accurate and the sources should be shown for each individual entry. They must be double checked for accuracy. Do NOT provide any preamble to the answer you provide. Just provide the summary. The summary should be constructed by critically evaluating the financials appearing in the context, with special focus of identifying risks. The output should be in HTML with apprpriate formatting (With footnote reference markers. References should include the document name, section and the page number if is available). The proper and beautiful formatting is crucial. Do not include any other thing apart from the correct HTML code. Do not include any preamble or disclaimer."

        self.risks = """
        Only output the HTML code of the analysis. It has to be directly incorporated into a webpage.
        
        Critically evaluate the key financial parameters for the latest year and the previous year and identify risks. Extract information privided by consolidated financials, auditor's report, management discussion and analysis, and other relevant sections. The risks should be identified in a critical stand-point, citing the exact financial values that were used to arrive at each conclusion. The output should be in HTML with apprpriate formatting (With footnote reference markers. References should include the document name, section and the page number if is available). Do not include any other thing apart from the correct HTML code. DO NOT include any preamble or disclaimer. Only the HTML code of the analysis should be provided. Do not output preambles like "Here is my analysis of the key financial risks based on the provided information:".
        
        """

        self.key = """Extract all the financial data that fallls under Assets, Liabilities, Equity,Revenue, Expenses, etc and all other Financial details that are mentioned in the given data and their values from the date given. do not miss any of the data. The accuracy of this is crucial. Mention the unit of price. Do NOT provide any preamble to the answer you provide. Provide the table with exactly correct values from the data given.
        """

        self.ratio_template = """Calculate key financial ratios that can be calculated from given financial data. Only output the ratios that can be calculated with provided data. Do not mention others.
         
        {key}.
        
        """

        self.ratio_formatter_template = """Present the key financial ratios as the code of HTML table. Make sure the table header contains name of the ratio, formula and the calculated value. Do not contain any additional thing in the answer apart from the table.
         
        {key}.
        
        """

        self.key_template = """Present the key financial parameters as the code of HTML table. Make sure the table header contains Parameter, Year and Value.  Mention the unit of price in value column. Do not contain any additional thing in the answer apart from the table.
         
        {key}.
        
        """

        self.critic_template = """Critically evaluate the finantial stats. Try to elicit credit risks associated with the company. Output should be the HTML code to be inserted into a webpage. Any risks identified should be highlihted by <span> with class name "risk". Provide a detailed analysis of the financial stats and the risks associated with the company. Do not include any other thing apart from the correct HTML code. Do not include any preamble or disclaimer.
         
        {key}.
        
        """

        self.assets = """Extract all the data related to company's assets including current and non-current assets and their values from the financial data given. Mention the unit of price. Use the heading "Assets". Do NOT provide any preamble to the answer you provide. Just provide the HTML code for the table with the correct values. The code should be able to be directly inserted into a webpage.
        """

        self.liabilities = """Extract all the data related to company's liabilities and their values from the data given. Mention the unit of price. Use the heading "Liabilities". Do NOT provide any preamble to the answer you provide. Just provide the HTML code for the table with the correct values. The code should be able to be directly inserted into a webpage.
        """

        self.equity = """Extract all the data related to company's equity and their values from the data given. Mention the unit of price. Use the heading "Equity". Do NOT provide any preamble to the answer you provide. Just provide the HTML code for the table with the correct values. The code should be able to be directly inserted into a webpage.
        """

        self.revenue = """Extract all the data related to company's revenue and their values from the data given. Mention the unit of price. Use the heading "Revenue". Do NOT provide any preamble to the answer you provide. Just provide the HTML code for the table with the correct values. The code should be able to be directly inserted into a webpage.
        """

        self.table_template = """Create a single table from these values. Use appropriate headings. output the html code for the table. Do not include any other thing aprt from the correct html code.
         
        {key}.
        
        """

        self.html_formal = """Write the HTML code with necessary formatting to present the financial stats. Output should be the HTML code to be inserted into a webpage. Any risks identified should be highlihted by <span> with class name "risk".
         
        {key}.
        
        """

        self.ns = """You are Neurasense AI, an expert credit analysit.
         
        {key}.
        
        """
