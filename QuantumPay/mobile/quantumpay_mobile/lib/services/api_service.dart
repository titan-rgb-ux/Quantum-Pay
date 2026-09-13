import 'dart:convert';
import 'package:http/http.dart' as http;
import '../config/api_config.dart';

class ApiService {
  Future<Map<String, dynamic>> get(String path) async {
    final r = await http.get(Uri.parse('${ApiConfig.baseUrl}$path'));
    return _decode(r);
  }

  Future<Map<String, dynamic>> post(String path, Map<String, dynamic> body) async {
    final r = await http.post(
      Uri.parse('${ApiConfig.baseUrl}$path'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode(body),
    );
    return _decode(r);
  }

  Map<String, dynamic> _decode(http.Response r) {
    final data = jsonDecode(r.body);
    if (r.statusCode < 200 || r.statusCode >= 300) {
      throw Exception(data is Map && data['detail'] != null ? data['detail'] : r.body);
    }
    return Map<String, dynamic>.from(data);
  }
}
