from flask import render_template

class View:
    @staticmethod
    def display_performance_report(report, report_name):
        return render_template('report.html', report=report, report_name=report_name)

    @staticmethod
    def display_report(report, report_name): 
        report_html = report.get_html()  # Get HTML for the report
        return render_template('report.html', report_html=report_html, report_name=report_name)

    @staticmethod
    def display_monitoring(reference_data, current_data):
        return render_template('monitoring.html', reference_data=reference_data, current_data=current_data)
