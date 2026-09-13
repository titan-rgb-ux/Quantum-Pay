import 'package:flutter/material.dart';

class TransactionResultScreen extends StatelessWidget {
  final String message;
  const TransactionResultScreen({super.key, required this.message});
  @override Widget build(BuildContext context) => Scaffold(
    appBar: AppBar(title: const Text('Transaction Result')),
    body: Center(child: Padding(padding: const EdgeInsets.all(20), child: Text(message))),
  );
}
