import 'api_service.dart';

class AuthService {
  final ApiService api;
  AuthService(this.api);

  Future<Map<String, dynamic>> createUser(String username, String displayName) =>
      api.post('/users', {'username': username, 'display_name': displayName});

  Future<Map<String, dynamic>> issueDemoKey(String username) =>
      api.post('/auth/issue-demo-key/$username', {});

  Future<Map<String, dynamic>> loginStart(String username) =>
      api.post('/auth/login/start', {'username': username});

  Future<Map<String, dynamic>> loginComplete(Map<String, dynamic> body) =>
      api.post('/auth/login/complete', body);
}
