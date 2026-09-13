import 'api_service.dart';

class TransactionService {
  final ApiService api;
  TransactionService(this.api);

  Future<Map<String, dynamic>> send({
    required String sender,
    required String receiver,
    required double amount,
    required String challenge,
    required String signature,
    required String credentialId,
  }) =>
      api.post('/transactions/create', {
        'sender': sender,
        'receiver': receiver,
        'amount': amount,
        'challenge': challenge,
        'signature': signature,
        'credential_id': credentialId,
      });

  Future<dynamic> history(String username) => api.get('/transactions/history/$username');
}
