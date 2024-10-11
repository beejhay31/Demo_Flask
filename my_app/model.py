from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from evidently.pipeline.column_mapping import ColumnMapping
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, TargetDriftPreset, DataQualityPreset

class Model:
    def __init__(self):
        # Initialize the logistic regression model and column mapping
        self.model = LogisticRegression(max_iter=200)
        self.column_mapping = ColumnMapping()
        self.column_mapping.target = 'target'
        self.column_mapping.prediction = 'prediction'
        self.column_mapping.numerical_features = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

    def train_model(self, reference_data, current_data):
        """
        Train the logistic regression model on reference data.
        """
        X_train = reference_data.drop(columns=['target'])
        y_train = reference_data['target']
        
        self.model.fit(X_train, y_train)
        return "Model training complete."

    def performance_report(self, reference_data, current_data):
        """
        Generate a performance report on the current data using the trained model.
        """
        X_test = current_data.drop(columns=['target'])
        y_test = current_data['target']
        predictions = self.model.predict(X_test)

        accuracy = accuracy_score(y_test, predictions)
        report = classification_report(y_test, predictions, output_dict=True)

        performance_report = {
            'accuracy': accuracy,
            'classification_report': report
        }

        return performance_report

    def target_report(self, reference_data, current_data):
        """
        Generate a target drift report between reference and current data.
        """
        target_drift_report = Report(metrics=[TargetDriftPreset()])
        target_drift_report.run(
            reference_data=reference_data,
            current_data=current_data,
            column_mapping=self.column_mapping
        )
        return target_drift_report

    def data_drift_report(self, reference_data, current_data):
        """
        Generate a data drift report between reference and current data.
        """
        data_drift_report = Report(metrics=[DataDriftPreset()])
        data_drift_report.run(
            reference_data=reference_data,
            current_data=current_data,
            column_mapping=self.column_mapping
        )
        return data_drift_report

    def data_quality_report(self, reference_data, current_data):
        """
        Generate a data quality report for the given reference and current data.
        """
        data_quality_report = Report(metrics=[DataQualityPreset()])
        data_quality_report.run(
            reference_data=reference_data,
            current_data=current_data,
            column_mapping=self.column_mapping
        )
        return data_quality_report
