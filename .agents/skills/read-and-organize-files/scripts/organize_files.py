import os
import shutil
import sys

def organize_workspace(base_dir='e:/file/3term1/AI'):
    """
    Automated script to detect new files in root workspace,
    categorize them, and move them to designated folders:
    - เอกสาร/
    - สไลด์/
    - แลบ/
    """
    dirs = {
        'เอกสาร': os.path.join(base_dir, 'เอกสาร'),
        'สไลด์': os.path.join(base_dir, 'สไลด์'),
        'แลบ': os.path.join(base_dir, 'แลบ')
    }
    
    for d in dirs.values():
        os.makedirs(d, exist_ok=True)
        
    system_dirs = {'.agents', '.agent', '.git', 'notes', 'เอกสาร', 'สไลด์', 'แลบ'}
    
    moved_count = 0
    for fname in os.listdir(base_dir):
        fpath = os.path.join(base_dir, fname)
        if os.path.isdir(fpath) or fname in system_dirs:
            continue
            
        target = None
        new_name = fname
        
        # Categorize
        if fname.startswith('Chapter-'):
            target = dirs['สไลด์']
        elif fname.startswith(('Lab-', 'lab-')) or 'l - ' in fname or fname in ['sudoku.pdf', 'ttt.pdf']:
            target = dirs['แลบ']
        elif fname.startswith(('บทที่ ', 'Sheet-', 'เอกสาร-')) or 'c.pdf' in fname or 'c.txt' in fname or 'c - ' in fname:
            target = dirs['เอกสาร']
        elif 'tobe' in fname.lower():
            target = dirs['เอกสาร']
            new_name = 'ใบสมัคร_TO_BE_NUMBER_ONE.pdf'
        else:
            # Default to เอกสาร for general documents/PDFs
            target = dirs['เอกสาร']
            
        if target:
            dest_path = os.path.join(target, new_name)
            shutil.move(fpath, dest_path)
            print(f"Moved: {fname} -> {os.path.basename(target)}/{new_name}")
            moved_count += 1
            
    print(f"Organization completed. Total files moved: {moved_count}")

if __name__ == '__main__':
    base = sys.argv[1] if len(sys.argv) > 1 else 'e:/file/3term1/AI'
    organize_workspace(base)
