#!/usr/bin/env python3
"""
Auto-generate quiz manifest from questions folder structure.
Chỉ cần tạo file JSON, script này tự động phát hiện và cập nhật manifest.
"""

import json
import os
from pathlib import Path

def generate_manifest():
    """Scan questions folder and generate manifest.json"""
    
    questions_dir = Path('questions')
    manifest = {
        'quizzes': [],
        'subjects': {}
    }
    
    # Emoji mapping cho các môn học
    subject_emojis = {
        'python': '🐍',
        'macroeconomics': '📊',
        'data-structures': '🗂️',
        'calculus': '📐',
        'statistics': '📈',
        'algorithms': '⚙️',
        'mp': '💼',
        'econometric': '📈',
        'dsa': '🔢',
        'database management system': '💾',
        'lich su dang': '📚',
        'ngan hang thuong mai': '🏦',
        'principle of accounting': '📊',
        'default': '📚'
    }
    
    # Scan tất cả file .json trong questions/
    for subject_folder in sorted(questions_dir.iterdir()):
        if not subject_folder.is_dir():
            continue
            
        subject_name = subject_folder.name
        subject_emoji = subject_emojis.get(subject_name, subject_emojis['default'])
        
        # Khởi tạo subject trong manifest
        if subject_name not in manifest['subjects']:
            manifest['subjects'][subject_name] = {
                'name': subject_name.replace('-', ' ').title(),
                'emoji': subject_emoji,
                'quizzes': []
            }
        
        # Tìm tất cả file .json trong subject folder
        json_files = sorted(subject_folder.glob('*.json'))
        
        for json_file in json_files:
            # Đọc file để đếm số câu hỏi
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    questions = json.load(f)
                    question_count = len(questions) if isinstance(questions, list) else 0
            except Exception as e:
                print(f"⚠️  Warning: Could not read {json_file}: {e}")
                question_count = 0
            
            # Tạo quiz ID từ đường dẫn
            lesson_name = json_file.stem  # Tên file không có .json
            quiz_id = f"{subject_name}-{lesson_name}"
            
            # Tạo display name từ file name
            display_name = lesson_name.replace('-', ' ').title()
            
            # Relative path từ root
            relative_path = str(json_file).replace('\\', '/')
            
            quiz_entry = {
                'id': quiz_id,
                'name': f"{subject_emoji} {manifest['subjects'][subject_name]['name']} - {display_name}",
                'file': relative_path,
                'subject': subject_name,
                'lesson': lesson_name,
                'questionCount': question_count,
                'description': f"{question_count} câu hỏi về {display_name}"
            }
            
            manifest['quizzes'].append(quiz_entry)
            manifest['subjects'][subject_name]['quizzes'].append(quiz_id)
    
    # Ghi manifest.json
    manifest_path = questions_dir / 'manifest.json'
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Generated manifest with {len(manifest['quizzes'])} quizzes")
    print(f"📁 Subjects: {', '.join(manifest['subjects'].keys())}")
    print(f"💾 Saved to: {manifest_path}")
    
    return manifest

if __name__ == '__main__':
    manifest = generate_manifest()
    
    # Print summary
    print("\n📊 SUMMARY:")
    for subject_name, subject_data in manifest['subjects'].items():
        print(f"\n{subject_data['emoji']} {subject_data['name']}:")
        for quiz_id in subject_data['quizzes']:
            quiz = next(q for q in manifest['quizzes'] if q['id'] == quiz_id)
            print(f"  - {quiz['lesson']}: {quiz['questionCount']} câu")
