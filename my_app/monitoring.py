import pandas as pd
from evidently.pipeline.column_mapping import ColumnMapping
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, TargetDriftPreset, DataQualityPreset
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

class Monitoring:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def monitor_performance(self, reference_data, current_data):
        performance_report = self.model.performance_report(reference_data, current_data)
        self.view.display_performance_report(performance_report, "Model Performance Report")
        return performance_report

    def monitor_drift(self, reference_data, current_data):
        drift_report = self.model.data_drift_report(reference_data, current_data)
        self.view.display_report(drift_report, "Data Drift Report")
        return drift_report

    def monitor_target_drift(self, reference_data, current_data):
        target_drift_report = self.model.target_report(reference_data, current_data)
        self.view.display_report(target_drift_report, "Target Drift Report")
        return target_drift_report
