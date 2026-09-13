import 'dart:convert';
import 'package:flutter/material.dart';
import '../services/api_service.dart';
import '../services/auth_service.dart';
import 'wallet_screen.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});
  @override State<LoginScreen> createState() => _LoginScreenState();
}
class _LoginScreenState extends State<LoginScreen> {
  final user = TextEditingController();
  String message = '';
  final auth = AuthService(ApiService());

  Future<void> login() async {
    try {
      final key = await auth.issueDemoKey(user.text.trim());
      final start = await auth.loginStart(user.text.trim());
      final challenge = start['challenge'] as String;

      // This starter does not expose the private key through the Flutter app.
      // Use the backend test client/Postman for the cryptographic login demo,
      // or replace this flow with Android Credential Manager/WebAuthn.
      setState(() => message =
        'Challenge created. For production, use Android Credential Manager/passkeys.\n${jsonEncode(key)}');
    } catch (e) { setState(() => message = e.toString()); }
  }

  @override Widget build(BuildContext context) => Scaffold(
    appBar: AppBar(title: const Text('Login')),
    body: Padding(padding: const EdgeInsets.all(20), child: Column(children: [
      TextField(controller: user, decoration: const InputDecoration(labelText: 'Username')),
      const SizedBox(height: 20),
      ElevatedButton(onPressed: login, child: const Text('Start Passkey Login')),
      const SizedBox(height: 20), Text(message)
    ])),
  );
}
