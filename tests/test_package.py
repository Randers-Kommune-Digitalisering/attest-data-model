"""Checks for the public model contract shipped in the package."""

import unittest

import attest_data_model as model


class PackageContractTests(unittest.TestCase):
    def test_public_models_share_metadata(self):
        tables = {
            "authorized_sagsbehandler": model.AuthorizedSagsbehandler,
            "attestation_request": model.AttestationRequest,
            "attestation_order": model.AttestationOrder,
            "received_record": model.ReceivedRecord,
            "order_event": model.OrderEvent,
            "notification": model.Notification,
        }
        self.assertEqual(set(model.Base.metadata.tables), set(tables))
        for table_name, mapped_class in tables.items():
            with self.subTest(table=table_name):
                self.assertIs(mapped_class.__table__, model.Base.metadata.tables[table_name])

    def test_public_enums_have_stable_database_values(self):
        enum_columns = (
            (model.AttestationOrder.status, model.OrderStatus),
            (model.ReceivedRecord.outcome, model.RecordOutcome),
            (model.Notification.notification_type, model.NotificationType),
            (model.Notification.status, model.NotificationStatus),
            (model.AuthorizedSagsbehandler.role, model.SagsbehandlerRoles),
        )
        for column, enum_class in enum_columns:
            with self.subTest(column=column):
                self.assertIs(column.type.enum_class, enum_class)
                self.assertEqual(column.type.enums, [member.value for member in enum_class])


if __name__ == "__main__":
    unittest.main()
