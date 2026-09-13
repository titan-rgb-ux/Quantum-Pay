import 'package:flutter/material.dart';
import '../services/api_service.dart';
import '../services/transaction_service.dart';

class SendMoneyScreen extends StatefulWidget {
  final String username;
  const SendMoneyScreen({super.key, required this.username});
  @override State<SendMoneyScreen> createState() => _SendMoneyScreenState();
}
class _SendMoneyScreenState extends State<SendMoneyScreen> {
  final receiver = TextEditingController();
  final amount = TextEditingController();
  String message = '';
  final service = TransactionService(ApiService());

  @override Widget build(BuildContext context) => Scaffold(
    appBar: AppBar(title: const Text('Send Money')),
    body: Padding(padding: const EdgeInsets.all(20), child: Column(children: [
      TextField(controller: receiver, decoration: const InputDecoration(labelText: 'Receiver')),
      TextField(controller: amount, keyboardType: TextInputType.number, decoration: const InputDecoration(labelText: 'Amount')),
      const SizedBox(height: 20),
      ElevatedButton(onPressed: () => setState(() => message = 'Connect this screen to the real passkey/WebAuthn assertion before enabling transactions.'), child: const Text('Authorize Transaction')),
      Text(message)
    ])),
  );
}
