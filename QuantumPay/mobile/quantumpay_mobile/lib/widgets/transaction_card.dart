import 'package:flutter/material.dart';

class TransactionCard extends StatelessWidget {
  final Map<String, dynamic> tx;
  const TransactionCard({super.key, required this.tx});

  @override
  Widget build(BuildContext context) => Card(
    child: ListTile(
      title: Text('${tx['receiver']}  ₹${tx['amount']}'),
      subtitle: Text('${tx['risk_level']} • ${tx['status']}'),
    ),
  );
}
