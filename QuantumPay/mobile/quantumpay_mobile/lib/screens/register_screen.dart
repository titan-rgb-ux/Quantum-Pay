import 'package:flutter/material.dart';
import '../services/api_service.dart';
import '../services/auth_service.dart';
import 'login_screen.dart';

class RegisterScreen extends StatefulWidget {
  const RegisterScreen({super.key});
  @override State<RegisterScreen> createState() => _RegisterScreenState();
}
class _RegisterScreenState extends State<RegisterScreen> {
  final user = TextEditingController();
  final name = TextEditingController();
  String message = '';
  final auth = AuthService(ApiService());

  Future<void> register() async {
    try {
      await auth.createUser(user.text.trim(), name.text.trim());
      final key = await auth.issueDemoKey(user.text.trim());
      setState(() => message = 'Account created. Demo credential issued. Credential ID: ${key['credential_id']}');
    } catch (e) { setState(() => message = e.toString()); }
  }
  @override Widget build(BuildContext context) => Scaffold(
    appBar: AppBar(title: const Text('Register')),
    body: Padding(padding: const EdgeInsets.all(20), child: Column(children: [
      TextField(controller: user, decoration: const InputDecoration(labelText: 'Username')),
      TextField(controller: name, decoration: const InputDecoration(labelText: 'Display name')),
      const SizedBox(height: 20),
      ElevatedButton(onPressed: register, child: const Text('Register')),
      const SizedBox(height: 20), Text(message),
      TextButton(onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (_) => const LoginScreen())), child: const Text('Go to Login'))
    ])),
  );
}
