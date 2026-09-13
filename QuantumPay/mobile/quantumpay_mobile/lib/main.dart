import 'package:flutter/material.dart';
import 'screens/welcome_screen.dart';

void main() {
  runApp(const QuantumPayApp());
}

class QuantumPayApp extends StatelessWidget {
  const QuantumPayApp({super.key});
  @override
  Widget build(BuildContext context) => MaterialApp(
    debugShowCheckedModeBanner: false,
    title: 'QuantumPay',
    theme: ThemeData(useMaterial3: true, colorSchemeSeed: Colors.deepPurple),
    home: const WelcomeScreen(),
  );
}
