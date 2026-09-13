import 'package:flutter/material.dart';
import 'register_screen.dart';
import 'login_screen.dart';

class WelcomeScreen extends StatelessWidget {
  const WelcomeScreen({super.key});
  @override
  Widget build(BuildContext context) => Scaffold(
    appBar: AppBar(title: const Text('QuantumPay')),
    body: Center(child: Column(mainAxisSize: MainAxisSize.min, children: [
      const Text('Hybrid Quantum Passkey Authentication'),
      const SizedBox(height: 20),
      ElevatedButton(onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (_) => const RegisterScreen())), child: const Text('Create Account')),
      ElevatedButton(onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (_) => const LoginScreen())), child: const Text('Login')),
    ])),
  );
}
