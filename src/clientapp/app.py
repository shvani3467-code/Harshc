// pubspec.yaml dependencies
dependencies:
  firebase_core: ^3.0.0
  firebase_auth: ^5.0.0
  cloud_firestore: ^5.0.0
  firebase_storage: ^12.0.0

// main.dart - Login screen
import 'package:firebase_auth/firebase_auth.dart';

void loginUser(String phone) {
  FirebaseAuth.instance.verifyPhoneNumber(
    phoneNumber: phone,
    verificationCompleted: (PhoneAuthCredential cred) async {
      await FirebaseAuth.instance.signInWithCredential(cred);
    },
    // ... baaki OTP logic
  );
}

// chat screen - Firestore me message save hoga
FirebaseFirestore.instance.collection('chats').add({
  'sender': userId,
  'message': text,
  'timestamp': FieldValue.serverTimestamp()
});
