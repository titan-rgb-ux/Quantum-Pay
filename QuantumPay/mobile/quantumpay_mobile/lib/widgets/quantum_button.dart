import 'package:flutter/material.dart';

class QuantumButton extends StatelessWidget {
  final String text;
  final VoidCallback? onPressed;
  const QuantumButton({super.key, required this.text, this.onPressed});

  @override
  Widget build(BuildContext context) =>
      ElevatedButton(onPressed: onPressed, child: Text(text));
}
